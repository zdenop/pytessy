# -*- coding: utf-8 -*-

"""A setuptools based setup module.
"""

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="pytessy",
    version="0.1.1",
    author="hyperrixel",
    author_email="python@hyperrixel.com",
    description="Faster access to Tesseract-OCR from Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hyperrixel/pytessy",
    keywords="tesseract Tesseract-OCR",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=["numpy"],
    extras_require={
        "dev": ["flake8", "pytest"],
        "test": ["coverage", "Pillow"],
    },
    test_suite='tests',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Documentation": "https://pytessy.readthedocs.io/",
        "Bug Tracker": "https://github.com/hyperrixel/pytessy/issues",
        "Source": "https://github.com/hyperrixel/pytessy",
        "Projects": "https://hyperrixel.github.io/",
        "Homepage": "https://www.hyperrixel.com/",
    },
)
