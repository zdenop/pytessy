#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

import cv2
import pytessy.pytessy as pytessy
from PIL import Image, ImageFilter

if __name__ == "__main__":

    # Create pytessy instance
    ocrReader = pytessy.PyTessy()

    files = ["tests/testWord.png", "tests/5.4321.png"]
    root_dir = pathlib.Path(__file__).parents[1]

    # PIL Example
    for file in files:
        # Load Image
        img = Image.open(pathlib.Path(root_dir, file))
        # Scale up image
        w, h = img.size
        img = img.resize((2 * w, 2 * h))
        # Sharpen image
        img = img.filter(ImageFilter.SHARPEN)
        # Convert to ctypes
        imgBytes = img.tobytes()
        bytesPerPixel = int(len(imgBytes) / (img.width * img.height))
        # Use OCR on Image
        imageStr = ocrReader.read(
            img.tobytes(),
            img.width,
            img.height,
            bytesPerPixel,
            raw=True,
            resolution=600,
        )

        print(file, imageStr.decode("utf-8"))

    # OpenCV  example #1
    file = str(pathlib.Path(root_dir, files[0]))
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bytesPerPixel = int(len(img.tobytes()) / (img.shape[1] * img.shape[0]))
    imageStr = ocrReader.read(img.tobytes(), img.shape[1], img.shape[0], bytesPerPixel)
    print(file, imageStr)

    # OpenCV  example #2
    file = str(pathlib.Path(root_dir, files[1]))
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imageStr = ocrReader.readnp(img)
    print(file, imageStr)
