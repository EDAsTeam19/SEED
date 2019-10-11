import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SEED_pkg",
    version="0.0.1",
    author="Valentín Calzada-Ledesma and Juan de Anda-Suárez",
    author_email="valetin.cl@purisima.tecnm.mx, juan.ds@purisima.tecnm.mx",
    description="Implementation of SEED algorithm for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EDAsTeam19/SEED.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
