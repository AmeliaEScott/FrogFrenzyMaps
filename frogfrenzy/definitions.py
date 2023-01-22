

class Definitions:
    class AnimatedBitmap:
        def __init__(self, line):
            self.name = ""
            self.frame_bitmaps = []
            self.frame_times = []

            self.name, line = line.split("=")
            self.name = self.name.strip()

            data = line.split(",")
            for i in range(0, len(data), 2):
                self.frame_bitmaps.append(data[i].strip())
                self.frame_times.append(int(data[i + 1].strip()))

    class Tile:
        def __init__(self, line):
            number, line = line.split("=")
            self.number = int(number.strip())
            line = line.strip().split(",")
            self.up, self.down, self.left, self.front, self.right, self.back = \
                map(lambda t: None if t.strip() == "NULL" else t.strip(), line)

    class Sprite:
        def __init__(self, line):
            number, line = line.split("=")
            self.number = int(number.strip())
            line = line.split(",")
            self.default_bitmap = line[0].strip()
            line = map(lambda t: int(t.strip()), line[1:])
            self.height = next(line)
            self.size = next(line)
            self.transparency = next(line)
            self.skills = list(line)

    def __init__(self, path):
        self.world_size = 0
        self.world_height = 0
        self.block_size = 0
        self.floor_texture_size = 0
        self.wall_texture_size = 0
        self.wall_texture_height = 0
        self.start_x = 0
        self.start_z = 0
        self.distance_perspective_correct = 0
        self.background_bitmap = None
        self.background_width = 0
        self.background_height = 0

        self.floor_bitmaps = {}
        self.wall_bitmaps = {}
        self.sprite_bitmaps = {}

        self.animated_tile_bitmaps = {}
        self.animated_sprite_bitmaps = {}

        self.tiles = {}
        self.sprites = {}

        self.parse_file(path)

    def parse_file(self, path):
        with open(path, "r") as fp:
            for line in fp:
                # Remove newline characters
                line = line.strip()
                # Skip blank lines
                if len(line) < 1:
                    continue
                firstchar = line[0]
                line = line[1:]
                if firstchar == "@":
                    self.parse_variable(line)
                elif firstchar == "#":
                    self.parse_bitmap_floor(line)
                elif firstchar == "$":
                    self.parse_bitmap_wall(line)
                elif firstchar == "^":
                    self.parse_bitmap_sprite(line)
                elif firstchar == ">":
                    self.parse_animated_bitmap_tile(line)
                elif firstchar == "<":
                    self.parse_animated_bitmap_sprite(line)
                elif firstchar == "%":
                    self.parse_tile(line)
                elif firstchar == "&":
                    self.parse_sprite(line)
                elif firstchar == "*":
                    self.parse_moving_tile(line)
                elif firstchar == "+":
                    self.parse_moving_sprite(line)
                else:
                    pass  # Comments, blank lines, etc

    def parse_variable(self, line):
        var, val = line.split(" ")
        if var == "a":
            self.world_size = int(val)
        elif var == "b":
            self.world_height = int(val)
        elif var == "c":
            self.block_size = int(val)
        elif var == "d":
            self.floor_texture_size = int(val)
        elif var == "e":
            self.wall_texture_size = int(val)
        elif var == "f":
            self.wall_texture_height = int(val)
        elif var == "g":
            self.start_x = int(val)
        elif var == "h":
            self.start_z = int(val)
        elif var == "i":
            self.distance_perspective_correct = int(val)
        elif var == "j":
            bitmap, width, height = val.split(",")
            self.background_bitmap = bitmap
            self.background_width = int(width)
            self.background_height = int(height)
        else:
            raise RuntimeError(f"Unknown variable in def file \"{var}\" with value \"{val}\"")

    def parse_bitmap_wall(self, line):
        name, bitmap = line.split("=")
        self.wall_bitmaps[name.strip()] = bitmap.strip()

    def parse_bitmap_floor(self, line):
        name, bitmap = line.split("=")
        self.floor_bitmaps[name.strip()] = bitmap.strip()

    def parse_bitmap_sprite(self, line):
        name, bitmap = line.split("=")
        self.sprite_bitmaps[name.strip()] = bitmap.strip()

    def parse_animated_bitmap_tile(self, line):
        bmp = Definitions.AnimatedBitmap(line)
        self.animated_tile_bitmaps[bmp.name] = bmp

    def parse_animated_bitmap_sprite(self, line):
        bmp = Definitions.AnimatedBitmap(line)
        self.animated_sprite_bitmaps[bmp.name] = bmp

    def parse_tile(self, line):
        tile = Definitions.Tile(line)
        self.tiles[tile.number] = tile

    def parse_sprite(self, line):
        sprite = Definitions.Sprite(line)
        self.sprites[sprite.number] = sprite

    def parse_moving_tile(self, line):
        # TODO
        pass
    
    def parse_moving_sprite(self, line):
        # TODO
        pass