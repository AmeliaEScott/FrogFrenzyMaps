import numpy as np


class LevelMap:

    Tile = np.dtype([
        ("id", "<u2"),
        ("filler", "<u2"),
        ("corner_top_sw_height", "<i2"),
        ("corner_top_nw_height", "<i2"),
        ("corner_top_se_height", "<i2"),
        ("corner_top_ne_height", "<i2"),
        ("corner_bottom_sw_height", "<i2"),
        ("corner_bottom_nw_height", "<i2"),
        ("corner_bottom_se_height", "<i2"),
        ("corner_bottom_ne_height", "<i2"),
        ("brightness", "<i2"),
    ])

    Sprite = np.dtype([
        ("id", "<u2"),
        ("unknown", "55u1"),
        ("brightness", "<u2")
    ])

    def __init__(self, dims, path):
        self.path = path
        with open(path, "rb") as fp:
            self.data: np.ndarray = np.fromfile(fp, dtype=np.dtype("<i2"))

        total_size = self.data.shape[0]
        map_size = dims[0] * dims[1] * 11

        sprite_start = 4
        map_start = total_size - map_size

        self.sprites = self.data[sprite_start:map_start - 2]\
            .view(dtype=LevelMap.Sprite)\
            .reshape((-1))

        self.tiles = self.data[map_start:]\
            .reshape([dims[0], dims[1], 11])\
            .view(dtype=LevelMap.Tile)
        self.dims = self.data[map_start - 2:map_start]
        assert np.all(self.dims == self.tiles.shape[0:2])

        # self.data = self.data.reshape([-1, 11])

    def write(self):
        with open(self.path, "wb") as fp:
            self.data.tofile(fp)
