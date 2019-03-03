import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Console ANSI escape sequences",
    version="0.0.1",
    author="RMuskovets",
    author_email="rmuskovets@gmail.com",
    description="A collection of ANSI escape codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RMuskovets/pyescapes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)