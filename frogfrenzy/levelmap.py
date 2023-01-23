import numpy as np


class LevelMap:
    Tile = np.dtype([
        ("id", "<u2"),
        ("unknown", "<u2"),
        ("corner_top_sw_height", "<i2"),
        ("corner_top_nw_height", "<i2"),
        ("corner_top_se_height", "<i2"),
        ("corner_top_ne_height", "<i2"),
        ("corner_bottom_sw_height", "<i2"),
        ("corner_bottom_nw_height", "<i2"),
        ("corner_bottom_se_height", "<i2"),
        ("corner_bottom_ne_height", "<i2"),
        ("color", "<u1"),
        ("brightness", "<u1"),
    ])

    Sprite = np.dtype([
        ("id", "<u2"),
        # Changing unknown0 has no visible effect, but it has a lot of different values
        ("unknown0", "9u1"),
        ("flip_horiz", "b1"),
        ("flip_vert", "b1"),
        # Unknown1 is all zeros, except for 2 weird sprites on Level 20.
        # Changing them to non-zero seems to do nothing.
        ("unknown1", "20u1"),
        # This is the section where changing stuff starts to matter.
        # The first 4 bytes somehow affect X-position, but I haven't figured out how.
        ("unknown2", "4u1"),
        # Zeros1 is all zeros and doesn't change anything.
        ("zeros0", "4u1"),
        ("unknown4", "4u1"),
        # More zeros! More useless!
        ("zeros1", "4u1"),
        ("unknown6", "4u1"),
        # Changing tile_x and tile_y seems to do nothing. But looking
        # at the data, it sure seems to correlate with the location of the sprite!
        # (And yes, the order is Y then X. Weird, huh?)
        ("tile_y", "<u2"),
        ("tile_x", "<u2"),
        ("color", "<u1"),
        ("brightness", "<u1"),
    ])

    def __init__(self, path):
        self.path = path
        with open(path, "rb") as fp:
            self.data: np.ndarray = np.fromfile(fp, dtype=np.dtype("<i1"))

        total_size = self.data.shape[0]

        sprite_start = 8
        num_sprites = self.data[6:8].view(dtype="<u2")[0]
        map_start = sprite_start + (num_sprites + 1) * LevelMap.Sprite.itemsize + 4
        self.dims = self.data[map_start - 4:map_start] \
            .view(dtype="<u2")
        map_size = self.dims[0] * self.dims[1] * LevelMap.Tile.itemsize
        map = self.data[map_start:map_start + map_size * 2] \
            .view(dtype="<u2")

        self.sprites = self.data[sprite_start: sprite_start + (num_sprites + 1) * LevelMap.Sprite.itemsize] \
            .view(dtype=LevelMap.Sprite) \
            .reshape((-1))

        self.tiles = map \
            .reshape([self.dims[0], self.dims[1], 11]) \
            .view(dtype=LevelMap.Tile)

        assert np.all(self.dims == self.tiles.shape[0:2])

        # self.data = self.data.reshape([-1, 11])

    def write(self):
        with open(self.path, "wb") as fp:
            self.data.tofile(fp)
