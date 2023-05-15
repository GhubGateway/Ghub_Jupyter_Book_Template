## https://github.com/rljbufny1/ghub_jupyter_book_template

- Procedure and template files for hosting a Jupyter Book Github tool on Ghub.<br>
- See https://theghub.org for more information on the Ghub Science Gateway.<br> 
- See Jupyter Book Zenodo reference: https://doi.org/10.5281/zenodo.2561065 for more information on Jupyter Book.

### Requirements:

#### notebooks directory

This directory contains the Jupyter Notebooks displayed by the Jupyter Book.

#### jupyter_book_build_dir directory

This directory contains the _config.yml and _toc.yml files as well as additional files required   Jupyter Book including index.md and user_manual.md.

This directory also contains a link to the notebooks directory. Used ln -s ../notebooks notebooks to create the link.

#### src directory

This directory contains the Makefile which builds the Jupyter Book on Ghub.

#### middleware directory
This directory contains the invoke script which enables the Jupyter Book to be launched on Ghub

#### Install the packages per ./setup.py, enter:

```
use -e -r anaconda-7
python -m pip install . --target ./lib
```

#### If required, create an environment per ./environment.yml and install packages per ./setup.py to the created environment, enter:

```
use -e -r anaconda-7
conda env create -f environment.yml --prefix ./env
conda activate ./env
python -m pip install . --target ./lib

```

### Create New Tool on Ghub:

Follow the instructions on the https://theghub.org/tools/create web page. Select the Repository Host, Host GIT repository on Github. Select the Publishing Option, Jupyter Notebook.  

Note: created tools are launched from the Ghub Dashboard's My Tools component.

### Notes:

Current web browser results:

Firefox, Google Chrome, Microsoft Edge and Safari, Jupyter Book aligned properly, image displays and links work.<br>
