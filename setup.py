from setuptools import find_packages
from setuptools import setup

setup(
    name="z-zytome",
    version="0.0.26",
    description="Zytome is declarative library for handling gene expression data for various data portals or datasets.",
    url="https://github.com/mzguntalan/zytome",
    author="Marko Zolo Gozano Untalan",
    author_email="mzguntalan@gmail.com",
    license="Apache-2.0",
    packages=find_packages(),
    install_requires=["anndata>=0.12.1", "numpy>=2.2.6"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
)
