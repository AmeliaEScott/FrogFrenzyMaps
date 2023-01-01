# from matplotlib import pyplot as plt; import numpy as np; import main; arr = main.read_file("LEVEL/LEVEL0.MAP")
import frogfrenzy
import numpy as np


level0map = frogfrenzy.LevelMap((42, 42),
        "/Users/Timmy/VirtualBox VMs/Shared Folder/3D Frog Frenzy (Unmodified)/LEVEL/LEVEL0.MAP")
level1map = frogfrenzy.LevelMap((42, 42),
        "/Users/Timmy/VirtualBox VMs/Shared Folder/3D Frog Frenzy (Unmodified)/LEVEL/LEVEL1.MAP")


def cheat_level0():
    level0map.tiles[13, 7, 0] = 100
    level0map.write()


def cheat_level1():
    pass

    level1map.write()


if __name__ == "__main__":
    cheat_level0()
    cheat_level1()
