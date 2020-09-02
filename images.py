import os
import sys
from PIL import Image


def convert_images(from_folder, to_folder):
    if not os.path.exists(to_folder):
        os.mkdir(to_folder)

    try:
        for image in os.listdir(from_folder):
            image_name = os.path.splitext(image)[0]

            img = Image.open(f"{from_folder}{image}")
            img.save(f"{to_folder}{image_name}.png", "png")
    except FileNotFoundError:
        sys.exit(
            f"We didn't find {from_folder} folder. Please, provide existing folder with images you want to convert")


if __name__ == "__main__":
    from_folder = sys.argv[1]
    to_folder = sys.argv[2]
    convert_images(from_folder, to_folder)
