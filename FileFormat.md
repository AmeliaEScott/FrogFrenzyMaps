# MAP file format

Map files are binary files, arranged in the following format. Unless otherwise
specified, most data is little-endian 16-bit integers (some signed, some unsigned).

All byte ranges are left-inclusive, right-exclusive, just like Numpy index syntax.
For example, "Bytes 0-2" includes Bytes 0 and 1, but not 2.

I am still unsure of some specifics, which I have marked with `?`.

- Bytes 0-4: Sprite header
  - Bytes 0-2: Unknown `?`
  - Bytes 2-4: Number of sprites (unsigned)
- Bytes 5-63: Pointer sprite. I think this sprite is used in the level editor,
  but not in the actual game. `?`
- Bytes 63 - `(number_of_sprites * 59) + 63`: Array of sprites. Each sprite is 59 bytes,
  organized as follows:
  - Bytes 0-2: Sprite ID. This corresponds to the sprite IDs in the `.DEF` file (I.e., 
    all lines starting with `&`)
  - Bytes 2-57: I have no idea. Somewhere in here is the sprite's position, orientation,
    probably size, but I have not had time to sort it out.
  - Bytes 57-59: Brightness level, in a range of 0-3840. `?`: What is the significance of this number?
- Bytes `(number_of_sprites * 59) + 63` - `(number_of_sprites * 59) + 63 + 4`: Number of tiles,
  as 2 unsigned 16-bit ints (Width and height)
- Bytes `(number_of_sprites * 59) + 63 + 4` - end of file: Tiles. Each tile is 22 bytes, organized into
  11 16-bit ints, as follows:
  - Bytes 0-2: Tile ID. This corresponds to the tile ID in the `.DEF` file (I.e.,
    all lines starting with `%`)
  - Bytes 2-4: Unknown `?`
  - Bytes 4-20: Height of each corner of the tile. This is used to warp tiles into
    non-cube shapes, like ramps, and to create height differences between tiles. They are
    organized as 8 signed 16-bit integers, in the following order:
    - Top Southwest
    - Top Northwest
    - Top Southeast
    - Top Northeast 
    - Bottom Southwest
    - Bottom Northwest
    - Bottom Southeast
    - Bottom Northeast
  - Bytes 20-22: Brightness, in range 0-3840. `?`: What is the significance of this number?