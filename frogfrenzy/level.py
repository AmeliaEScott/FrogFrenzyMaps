from frogfrenzy import Definitions, LevelMap, Config
import os


class Level:

    def __init__(self, path):
        path, extension = os.path.splitext(path)
        if extension.upper() not in [".TXT", ".MAP", ".DEF"]:
            raise RuntimeError(f"Invalid file extension: {extension}")
        self.definitions = Definitions(path + ".DEF")
        self.level_map = LevelMap(path + ".MAP")
        self.config = Config(path + ".TXT")

    def write(self):
        self.level_map.write()
        # TODO: self.definitions.write()
