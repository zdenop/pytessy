# PyTessy - Tesseract-OCR, faster!

This module allows faster access to Tesseract-OCR from Python scripts.

## Quick start
This repository integrate changes from following [pytessy](https://github.com/hyperrixel/pytessy) forks:
* [sydneyprovence/pytessy](https://github.com/sydneyprovence/pytessy)
* [tbattz/pytessy](https://github.com/tbattz/pytessy)
* [jevgienij/pytessy](https://github.com/jevgienij/pytessy)
* [giorgiococci/pytessy](https://github.com/giorgiococci/pytessy) - Docker and FastAPI example

It adds more functionality:

* Allows using pytessy on Linux
* Allows pytessy to be used within a Jupyter notebook
* Allows to reads text from image data contained in a numpy ndarray

Note that you may need to import pytessy before/after importing numpy, as there seems to be something conflicting when importing in a certain order.

On linux, install tesseract and get the trained data.
```bash
sudo apt install tesseract-ocr
wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata
sudo mkdir /usr/share/tessdata/
sudo mv eng.traineddata /usr/share/tessdata/
```

Run the example usage script.

```bash
python3 examples/exampleUsage.py
```

Or run the following

```python
import pytessy.pytessy as pytessy
from PIL import Image, ImageFilter

# Create pytessy instance
ocrReader = pytessy.PyTessy()

files = ["tests/testWord.png", "tests/5.4321.png"]


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

	print(file, imageStr.decode("utf-8")
```

To build and run the docker container:
```
docker build . -t test-pytessy
docker run --rm -it  -p 80:80/tcp test-pytessy:latest
```

To run fastapi example (modify paths/filenames in exampleFastAPI.apy:
```
pip install fastapi "uvicorn[standard]"
cd examples
uvicorn exampleFastAPI:app --reload
```


## Why and when is it so fast?

PyTessy uses direct library-level access to Tesseract-OCR's core library. Therefore is it so fast in case when the image is already in the memory or when the image need to be processed before scanning with Tesseract-OCR. In case of reading and scanning existing files only PyTessy is just a bit faster than usual Tesseract-OCR Python wrappers.

## Requirements

### Operating system

PyTessy is operating system independent in case if you set the exact location of your Tesseract-OCR library since presently library search process is implemented on Windows only.

### Python modules

PyTessy uses only modules from the Standard Library only. Python version must be ` >= 3.6 `.

### External requirements

You have to have installed or portable version of Tesseract-OCR (at least a working library and ` tessdata `).

You can download Tesseract-OCR from [here](https://tesseract-ocr.github.io/tessdoc/Downloads).
For windows you [Tesseract installer for Windows from UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
Windows build with MSVC/clang does not work (for the moment)

## Installation

You can install the latest PyTessy version with ` pip install pytessy ` or you can download the wheel from this repository or you can build it from the source code.

To install development code (wheel filename could be different):

```
git clone https://github.com/zdenop/pytessy.git
cd pytessy
pip install .
python3 setup.py test
```

or

```
python3 -m pip install -e git+https://github.com/zdenop/pytessy.git
python3 setup.py test
```


## Documentation

PyTessy has a [ReadTheDocs page](https://pytessy.readthedocs.io/)
