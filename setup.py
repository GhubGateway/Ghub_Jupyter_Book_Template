# A minimal setup.py file to make a Python project installable.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

#with open("requirements.txt", "r") as fh:
#    requirements = [line.strip() for line in fh]
# Note: Requirements are satisfied by using the /apps/share64/debian10/anaconda/anaconda-7/envs/??? environment


setuptools.setup(
    name             = "Utils",
    version          = "0.1.0",
    author           = "rljbufny1",
    author_email     = "rljbufny1@gmail.com",
    description      = "Python utility module for ghub exercise 2.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages         = setuptools.find_packages(),
    classifiers       = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
    python_requires  = '>= 3.8',
    #install_requires = requirements,
)
