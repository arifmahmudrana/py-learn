"""
Usage: python3 ImagetoThumbnailconverter.py './Pokedex/**/*.jpg' 'x/x/c/v'
"""

import glob
import os
from sys import argv
from pathlib import Path
from PIL import Image, ImageFilter

files, target = argv[1], argv[2]

Path(target).mkdir(parents=True, exist_ok=True)
for file in glob.glob(files, recursive=True):
    img = Image.open(file)
    img.thumbnail((100, 100))
    img.save(os.path.join(target, os.path.basename(file)))
