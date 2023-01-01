import numpy as np


class LevelMap:
    def __init__(self, dims, path):
        self.path = path
        with open(path, "rb") as fp:
            self.data: np.ndarray = np.fromfile(fp, dtype=np.dtype("<i2"))

        total_size = self.data.shape[0]
        map_size = dims[0] * dims[1] * 11
        header_size = total_size - map_size

        self.header = self.data[0:header_size]
        self.tiles = self.data[header_size:].reshape([dims[0], dims[1], 11])

        # self.data = self.data.reshape([-1, 11])

    def write(self):
        with open(self.path, "wb") as fp:
            self.data.tofile(fp)