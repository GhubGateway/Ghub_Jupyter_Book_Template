# https://github.com/rljbufny1/ghub_vub_exercise2

- Exercise to download a SRTM 30m Global 1 arc second V0003 DEM for a selected volcano and convert the DEM to GRASS GIS raster format.
- Demonstrates installing a Jupyter Book Github project on Ghub.
- Demonstrates running a Ghub Pegasus workflow with python scripts.

## To install on Ghub

### Launch the Workspace 10 Tool and in a Terminal Widow enter:<br />

```
git clone https://github.com/rljbufny1/ghub_exercise1
```

### Create an environment per ./environment.yml:

```
conda env create -f environment.yml --prefix ./env --clone  
```

### Activate the created environment:

```
conda activate ./env
```

### Install the Utils package to the created enviromnent per ./setup.py:

```
python -m pip install . -- target ./lib
```

### To run on Ghub:

### Launch  the Jupyter on Deb10 Tool:<br />
Open ghub_exercise1/ghub_exercise1.ipynb<br />
Click the Appmode button<br />
Set the Latitude and Longitude Coordinates<br />
Click the Run Workflow Button<br />

#### See https://theghub.org/about for more information on Ghub. 
#### See https://pegasus.isi.edu/about for more information on the Pegasus WMS. 
#### See https://www.mathworks.com/matlabcentral/fileexchange/10915-deg2utm?status=SUCCESS and https://www.mathworks.com/matlabcentral/fileexchange/10914-utm2deg?s_tid=FX_rc1_behavfor for more information on the Matlab coordinate conversion scripts used for this exercise.
