# from matplotlib import pyplot as plt; import numpy as np; import main; arr = main.read_file("LEVEL/LEVEL0.MAP")
import frogfrenzy
import numpy as np


level0map = frogfrenzy.Level(
    "/Users/Timmy/VirtualBox VMs/Shared Folder/3D Frog Frenzy (Unmodified)/LEVEL/LEVEL0.MAP")
level1map = frogfrenzy.Level(
    "/Users/Timmy/VirtualBox VMs/Shared Folder/3D Frog Frenzy (Unmodified)/LEVEL/LEVEL1.MAP")


def cheat_level0():
    # Road of bricks and grass to the finish
    level0map.level_map.tiles[:, 7]["id"] = 100
    level0map.level_map.tiles[1:14, 8]["id"] = 80
    level0map.level_map.tiles[1:14, 6]["id"] = 80

    # Crossways brick road
    level0map.level_map.tiles[12, :]["id"] = 100

    # Wood to mark starting location
    level0map.level_map.tiles[13, 7]["id"] = 104

    arrows = np.logical_or(
        np.logical_or(
            level0map.level_map.tiles["id"] == 3,
            level0map.level_map.tiles["id"] == 4,
        ),
        np.logical_or(
            level0map.level_map.tiles["id"] == 28,
            level0map.level_map.tiles["id"] == 29,
        )
    )
    level0map.level_map.tiles["id"][arrows] = 100

    # level0map.level_map.sprites["id"] = 64
    # Make sure Sprite 15 is the starting location
    level0map.level_map.sprites[15]["id"] = 1

    # level0map.level_map.sprites[15]["unknown"][-4] = 12
    level0map.write()


if __name__ == "__main__":
    cheat_level0()
