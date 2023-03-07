# https://github.com/rljbufny1/ghub_exercise2

- Demonstrates installing a Jupyter Book Github project on Ghub.

## To install on Ghub

### Launch the Workspace 10 Tool and in a Terminal Widow enter:<br />

```
git clone https://github.com/rljbufny1/ghub_exercise2
```

or 

```
wget https://github.com/rljbufny1/ghub_exercise2/releases/download/v1.0.0/ghub_exercise2-src.tar.gz

tar xvzf ghub_exercise2-src.tar.gz

```

### Create an environment per ./environment.yml:

```
use -e -r anaconda-7
conda env create -f environment.yml --prefix ./env
```

### Install the Utils package to the created environment per ./setup.py:

```
conda activate ./env
python -m pip install . --target ./lib
```

### Addtional Requirements

#### landing page jupyter notebook

The landing page jupyter notebook contains the calls to run jupyter-book.

Example:

ghub_exercise2_landing_page.ipynb

#### middleware directory invoke script

The middleware directory invoke script enables the landing page jupyter notebook to be launched on Ghub.

Example:

#!/bin/sh

bindir="$(dirname "$(pwd)")"/bin<br />
libdir="$(dirname "$(pwd)")"/lib<br />
export PYTHONPATH=$PYTHONPATH:${bindir}:${libdir}<br />
/usr/bin/invoke_app "$@" -C "start_jupyter -A -T @tool ghub_exercise2_landing_page.ipynb" -t ghub_exercise2 -u anaconda-7 -r none

#### jupyter-book directory

The jupyter-book directory contains the _config.yml and _toc.yml files as well as 
additional files required by the Jupyter Book, for example, index.md.

This directory also contains the link to the actual notebooks displayed by the Jupyter Book,
for example, use ln -s ../notebooks notebooks to create thre link.

## To run on Ghub:

### Launch  the Jupyter Notebooks (202210) tool:<br />

Open ghub_exercise2/ghub_exercise2.ipynb.<br />
Click the Appmode button.<br />
Select a volcano.<br />
Click the Run Workflow Button.<br />

#### See https://theghub.org/about for more information on Ghub. 
#### See https://www.buffalo.edu/ccr.html for more information on CCR.
#### See https://pegasus.isi.edu/about for more information on the Pegasus WMS.
#### See https://jupyterbook.org/en/stable/intro.html for more information on Jupyter Book.
