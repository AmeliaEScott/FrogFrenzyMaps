# 3D Frog Frenzy

This is a library for interacting with level maps from
[3D Frog Frenzy](https://www.youtube.com/watch?v=tjwuZoFQWrg).

This is not a GUI or level editor, but it will hopefully make it easier
for someone else to make a GUI.

## Current Status

Working:

- Parsing Tiles into a useful Numpy array
- Separating raw bytes of individual Sprites
- Writing Tiles and Sprites to `.MAP` file
- Parsing `.DEF` files into `Definitions` objects

In progress:

- Reverse-engineering Sprite data. I have no idea what 55 out of 59
  bytes do for Sprites. If you figure it out, please submit a pull request!
- Better documentation

TODO:

- Write `Definitions` objects to `.DEF` files
- Error-checking

Will never be done by me:

- Any sort of GUI. If you want a GUI, you'll need to build it yourself on
  top of this library. But I'd be happy to help you use this library!
