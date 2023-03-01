# https://github.com/rljbufny1/ghub_vub_exercise2

- Exercise to download a SRTM 30m Global 1 arc second V0003 DEM for a selected volcano and convert the DEM to GRASS GIS raster format.
- Demonstrates installing a Jupyter Book Github project on Ghub.
- Demonstrates running a Ghub Pegasus workflow with python scripts on the CCR.

## To install on Ghub

### Launch the Workspace 10 Tool and in a Terminal Widow enter:<br />

```
git clone https://github.com/rljbufny1/ghub_vhub_exercise2
```

or 

```
wget https://github.com/rljbufny1/ghub_vhub_exercise2/releases/download/v1.0.0/ghub_vhub_exercise2-src.tar.gz

tar xvzf ghub_vhub_exercise2-src.tar.gz

```

### Create an environment per ./environment.yml:

```
use -e -r anaconda-7
conda env create -f environment.yml --prefix ./env
```
Note: 

Had to explicitly install python -m pip install cartopy==0.18.0 --target ./lib
(cartopy 0.21.0 requires GEOS 3.7.2 but GEOS 3.7.1 is currently installed.)

Had to explicitly install python -m pip install hublib --target ./lib

### Install the Utils package to the created environment per ./setup.py:

```
conda activate ./env
python -m pip install . --target ./lib
```

### To run on Ghub:

### Launch  the Jupyter Notebooks (202210):<br />
Open ghub_exercise1/ghub_vhub_exercise2.ipynb.<br />
Click the Appmode button.<br />
Select a volcano.<br />
Click the Run Workflow Button.<br />

#### See https://theghub.org/about for more information on Ghub. 
#### See https://www.buffalo.edu/ccr.html for more information on CCR.
#### See https://pegasus.isi.edu/about for more information on the Pegasus WMS.
