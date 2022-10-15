import pytessy
from PIL import ImageFilter, Image
from pathlib import Path

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    # Create pytessy instance
    ocrReader = pytessy.PyTessy(
        tesseract_path="/usr/bin/tesseract",
        lib_path="/usr/bin/tesseract",
        data_path="/usr/share/tesseract-ocr/4.00/tessdata",
    )

    image_folder = Path("./testImages")

    file = image_folder / "example.png"

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
    )
    print(file, imageStr)

    return {"File": file, "ImageStr": imageStr}
