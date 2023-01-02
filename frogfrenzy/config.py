import re


class Config:
    def __init__(self, path):
        with open(path, "r") as fp:
            lines = fp.read().split('\n')

        self.water_tile = 0
        self.home_tile = 0
        self.level_title = {}
        self.level_title['eng'] = ""
        self.level_title['fra'] = ""
        self.level_title['spa'] = ""

        for line in lines:
            try:
                key, value = map(str.strip, line.split("="))
            except ValueError:
                key, value = (line, "")
            if key == "water_tile":
                self.water_tile = int(value)
            elif key == "home_tile":
                self.home_tile = int(value)
            elif key == "level_title.eng":
                self.level_title['eng'] = value
            elif key == "level_title.fra":
                self.level_title['fra'] = value
            elif key == "level_title.spa":
                self.level_title['spa'] = value
