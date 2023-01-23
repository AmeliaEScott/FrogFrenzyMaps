# import numpy as np; import main as m; import frogfrenzy as ff; nonzero = np.any(m.level0map.level_map.sprites["unknown1"], axis=0); np.set_printoptions(linewidth=120)
import frogfrenzy
from frogfrenzy import mapascii
import numpy as np


level0map = frogfrenzy.Level(
    "/Users/Timmy/VirtualBox VMs/Shared Folder/3D Frog Frenzy (Unmodified)/LEVEL/LEVEL0.MAP")
level1map = frogfrenzy.Level(
    "/Users/Timmy/VirtualBox VMs/Shared Folder/3D Frog Frenzy (Unmodified)/LEVEL/LEVEL1.MAP")


def get_level(i):
    return frogfrenzy.Level(
        f"/Users/Timmy/VirtualBox VMs/Shared Folder/3D Frog Frenzy (Unmodified)/LEVEL/LEVEL{i}.MAP")


def get_all_levels():
    levels = []
    for i in range(0, 22):
        levels.append(get_level(i))
    return levels


def is_all_zero(levels, label):
    for i, l in enumerate(levels):
        z = np.any(l.level_map.sprites[label])
        print(f"Level {i} has nonzero {label}: {z}")

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
    level0map.level_map.sprites[13]["id"] = 78
    # Make sure Sprite 15 is the starting location
    level0map.level_map.sprites[15]["id"] = 1

    level0map.write()


if __name__ == "__main__":
    cheat_level0()
