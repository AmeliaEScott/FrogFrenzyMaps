#!/usr/bin/env python3
import argparse
import os
from PIL import Image
import shutil


def convert(file_in, file_out):
    # print(f"Converting {file_in} to {file_out}")
    with Image.open(file_in) as image_in:
        image_in.save(file_out)


parser = argparse.ArgumentParser(
    prog="convert_pcx.py",
    description="Bulk convert .pcx to .png files"
)

parser.add_argument(
    "-i", "--input",
    help="Path to the folder containing the .pcx files.",
    required=True
)

parser.add_argument(
    "-o", "--output",
    help="Path to the folder to which converted images should be saved.",
    required=True
)

args = parser.parse_args()

for dirpath, dirnames, filenames in os.walk(args.input):
    new_dir = os.path.join(args.output, dirpath.removeprefix(args.input))
    os.makedirs(new_dir, exist_ok=True)
    for filename in filenames:
        original_file = os.path.join(dirpath, filename)
        new_file = os.path.join(new_dir, filename)
        if filename.endswith(".PCX"):
            new_file = new_file.removesuffix(".PCX") + ".PNG"
            # print(f"Converting {original_file} to {new_file}")
            convert(original_file, new_file)
        else:
            # print(f"Copying {original_file} to {new_file}")
            shutil.copy(original_file, new_file)