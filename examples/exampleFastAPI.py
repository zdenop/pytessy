#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

import pytessy.pytessy as pytessy
from fastapi import FastAPI
from PIL import Image, ImageFilter

app = FastAPI()


@app.get("/")
async def root():
    # Create pytessy instance
    ocrReader = pytessy.PyTessy(
        # tesseract_path="/usr/bin/tesseract",
        # lib_path="/usr/bin/tesseract",
        # data_path="/usr/share/tesseract-ocr/4.00/tessdata",
    )

    root_dir = pathlib.Path(__file__).parents[1]
    image_folder = pathlib.Path(root_dir, "tests")

    file = image_folder / "testWord.png"

    # Load Image
    img = Image.open(file)

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
        img.tobytes(), img.width, img.height, bytesPerPixel, raw=True, resolution=600
    ).decode("utf-8")
    print(file, imageStr)

    return {"File": file, "ImageStr": imageStr}
