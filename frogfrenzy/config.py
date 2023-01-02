import re


class Config:

    class Level:
        def __init__(self, text):
            self.water_tile = 0
            self.home_tile = 0
            self.level_title_eng = ""
            self.level_title_fra = ""
            self.level_title_spa = ""

            for line in text.split("\n"):
                try:
                    key, value = map(str.strip, line.split("="))
                except ValueError:
                    key, value = (line, "")
                if key == "water_tile":
                    self.water_tile = int(value)
                elif key == "home_tile":
                    self.home_tile = int(value)
                elif key == "level_title.eng":
                    self.level_title_eng = value
                elif key == "level_title.fra":
                    self.level_title_fra = value
                elif key == "level_title.spa":
                    self.level_title_spa = value

    def __init__(self, path):
        with open(path, "r") as fp:
            text = fp.read()

        text = re.split(r"(\[[a-zA-Z]+\]\n)", text)[1:]
