import cv2
from PIL import Image, ImageFilter

import pytessy

if __name__ == "__main__":

    # Create pytessy instance
    ocrReader = pytessy.PyTessy()

    files = ["testImages/testWord.png", "testImages/5.4321.png"]

    # PIL Example
    for file in files:
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
            img.tobytes(),
            img.width,
            img.height,
            bytesPerPixel,
            raw=True,
            resolution=600,
        )

        print(file, imageStr)

    # OpenCV  example
    img = cv2.imread(files[0])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    string = ocrReader.read(img.tobytes(), img.shape[1], img.shape[0], 1)
    print(file, imageStr)
