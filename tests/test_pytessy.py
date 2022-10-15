import unittest
import pathlib

from PIL import Image
from pytessy.pytessy import PyTessy


class TestPyTessy(unittest.TestCase):

    _test_dir = pathlib.Path(__file__).parent.resolve()
    _image_file = pathlib.Path(_test_dir, "testWord.png")

    def test_pytessy(self):
        ocrReader = PyTessy()
        img = Image.open(self._image_file)
        imgBytes = img.tobytes()
        bytesPerPixel = int(len(imgBytes) / (img.width * img.height))
        imageStr = ocrReader.read(
            imgBytes,
            img.width,
            img.height,
            bytesPerPixel,
            raw=True,
            resolution=300,
        )
        self.assertEqual(imageStr.decode("utf-8"), "Test Word\n")


if __name__ == "__main__":
    unittest.main()
