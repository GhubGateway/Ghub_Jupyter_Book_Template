## https://github.com/rljbufny1/ghub_exercise2

- Demonstrates installing a Jupyter Book Github project on Ghub.

### Requirements:

#### Landing page Jupyter Notebook

The landing page Jupyter Notebook, ghub_exercise2_landing_page.ipynb, contains the call to build the Jupyter Book.

#### Middleware directory invoke script

The middleware directory contains the script, invoke, which enables the landing page Jupyter Notebook to be launched on Ghub:

#!/bin/sh

#References:<br> 
#https://theghub.org/kb/development/deploy-styles-for-jupyter-tools<br>
#https://theghub.org/kb/development/invoke-scripts-for-jupyter-notebooks<br>
#-A: App Mode<br>

#Reference: https://help.hubzero.org/documentation/22/tooldevs/invoke:<br>
#-C: Command to execute for starting the tool<br>
#-T: Tool root directory<br>
#-t: Sets ${toolname}<br>
#-u: Set use scripts to invoke before running the tool<br>
#-r: Set RAPPTURE_VERSION<br>
#-p: Prepend to the PATH environment variable<br>

/usr/bin/invoke_app "$@" -C "start_jupyter -A -T @tool ghub_exercise2_landing_page.ipynb" -t ghub_exercise2 -u anaconda-7 -r none -p @tool/../${VERSION}/lib

#### Jupyter Book template directory

The Jupyter Book template directory, jupyter-book, contains the _config.yml and _toc.yml files as well as 
additional files required by the Jupyter Book, index.md and user_manual.md.

This directory also contains the link to the actual notebooks displayed by the Jupyter Book. Used ln -s ../notebooks notebooks to create the link.

### Install on Ghub:

#### Launch the Workspace 10 Tool and in a xterm terminal window enter:<br />

```
git clone https://github.com/rljbufny1/ghub_exercise2
```
or 
```
wget https://github.com/rljbufny1/ghub_exercise2/releases/download/V1.0.0/ghub_exercise2-src.tar.gz
tar xvzf ghub_exercise2-src.tar.gz
```

### Install the Utils package per ./setup.py, enter:

```
use -e -r anaconda-7
python -m pip install . --target ./lib
```

### If required, create an environment per ./environment.yml and install the Utils package per ./setup.py to the created environment, enter:

```
use -e -r anaconda-7
conda env create -f environment.yml --prefix ./env
conda activate ./env
python -m pip install . --target ./lib

```

### Launch on Ghub:

#### Launch  the Jupyter Notebooks (202210) tool:<br />

Open ghub_exercise2/ghub_exercise2.ipynb.<br />
Click the Appmode button.<br />

### References:

See https://theghub.org for more information on the Ghub Science Gateway.<br /> 
See https://jupyterbook.org/en/stable/intro.html for more information on Jupyter Book.
