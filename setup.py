import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cowfeed",
    version="0.0.1",
    install_requires=["feedparser", "bs4"],
    author="Angus Hollands",
    author_email="goosey15@gmail.com",
    description="A simple RSS wrapper to cowsay",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agoose77/cowfeed",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'cowfeed = cowfeed:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
