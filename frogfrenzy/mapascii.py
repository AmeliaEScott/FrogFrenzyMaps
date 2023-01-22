# from matplotlib import pyplot as plt; import numpy as np; import main; arr = main.read_file("LEVEL/LEVEL0.MAP")
import numpy as np
from frogfrenzy import LevelMap, Level
import os


def get_all_levels(directory):
    levels = []

    for i in range(22):
        level_name = f"LEVEL{i}.MAP"
        level_path = os.path.join(directory, level_name)
        levels.append(Level(level_path))
    return levels


def bitmap_name_to_char(str):
    if 'grass' in str:
        return '.'
    elif 'asphalt' in str:
        return '_'
    elif 'water' in str:
        return '/'
    elif 'brick' in str:
        return 'B'
    elif 'tunnel' in str:
        return '@'
    elif 'wood' in str:
        return 'W'
    elif 'marble' in str:
        return 'M'
    elif 'arrow' in str:
        if 'up' in str:
            return '^'
        elif 'down' in str:
            return 'v'
        elif 'left' in str:
            return '<'
        elif 'right' in str:
            return '>'
        else:
            return '?'
    elif 'home' in str:
        return '$'
    else:
        return '?'


def print_all_levels(levels):
    # for i in level.level_map.tiles:
    # for j in i:
    # for k in j:
    # try:
    # print(level.definitions.tiles[k["id"]].up, end=' ')
    # break
    # except KeyError:
    # print('NULL', end=' ')
    # print('\n')
    for level in levels:
        print(level.config.level_title['eng'])
        print('DEF (visual) dimensions: ' + str([level.definitions.world_size, level.definitions.world_height]))
        print('MAP (logical) dimensions: ' + str(np.flip(level.level_map.dims)))
        for i in level.level_map.tiles:
            for j in i:
                for k in j:
                    try:
                        print(bitmap_name_to_char(level.definitions.tiles[k["id"]].up), end=' ')
                        break
                    except KeyError:
                        print(' ', end=' ')
            print('')
