import numpy as np


class LevelMap:

    Tile = np.dtype([
        ("id", "<u2"),
        ("filler", "<u2"),
        ("corner_uaa_height", "<i2"),
        ("corner_uab_height", "<i2"),
        ("corner_uac_height", "<i2"),
        ("corner_uad_height", "<i2"),
        ("corner_daa_height", "<i2"),
        ("corner_dab_height", "<i2"),
        ("corner_dac_height", "<i2"),
        ("corner_dad_height", "<i2"),
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
