"""
   These are the unit tests for our pytessy
"""
import unittest
import pathlib

from PIL import Image
from pytessy.pytessy import PyTessy


class TestPyTessy(unittest.TestCase):
    """Used as pytessy testing"""
    _test_dir = pathlib.Path(__file__).parent.resolve()
    _image_file = pathlib.Path(_test_dir, "testWord.png")

    def test_pytessy(self):
        """Test read function with PIL/Pillow image"""
        ocr_reader = PyTessy()
        img = Image.open(self._image_file)
        img_bytes = img.tobytes()
        bytes_per_pixel = int(len(img_bytes) / (img.width * img.height))
        image_str = ocr_reader.read(
            img_bytes,
            img.width,
            img.height,
            bytes_per_pixel,
            raw=True,
            resolution=300,
        )
        self.assertEqual(image_str, b"Test Word\n")


if __name__ == "__main__":
    unittest.main()
