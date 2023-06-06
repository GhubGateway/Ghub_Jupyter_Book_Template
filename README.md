## https://github.com/rljbufny1/ghub_exercise2

- Procedure and template files for hosting a Jupyter Book Github tool on Ghub.<br>
- See https://theghub.org for more information on the Ghub Science Gateway.<br> 
- See Jupyter Book Zenodo reference: https://doi.org/10.5281/zenodo.2561065 for more information on Jupyter Book.

### Requirements:

#### notebooks directory

This directory contains the Jupyter Notebooks ending in .ipynb contained  by the Jupyter Book. 

The name of this directory must be consistent with the link to this directory specified in the jupyter_book_contents directory and the name of this directory specified in the jupyter_book_contents/_toc.yml file.

#### jupyter_book_contents directory

This directory contains the Jupyter Book configuration file, _config.yml, and the Jupyter Book table of contents file, _toc.yml, as well as additional markdown files required to build the Jupyter Book including index.md and user_manual.md.

This directory also contains a link to the notebooks directory. Used ln -s ../notebooks notebooks to create the link.

The name of this directory must be consistent with the name of this directory specified in the src/Makefile and bin/showbook.sh files.

#### src directory

This directory contains the Makefile which contains the command to generate the Jupyter Book's HTML files on Ghub: jupyter-book build --all jupyter_book_contents. The generated HTML files are placed in the jupyter_book_contents/_build/html  directory.

To install the Makefile, launch the Workspace 10 Tool from the Ghub Dashboard's My Tools component and in a xterm terminal window, 
cd to the src directory and enter:<br />

use -e -r anaconda-7<br />
make install

#### bin directory

This directory contains the showbook.sh script to view the Jupyter Book's HTML files using a web browser.

Note: the showbook.sh script must have the executable file permissions bits set. For example, use chmod 755 showbook.sh  to set the executable file permission bits.

#### middleware directory

This directory contains the invoke script which enables the Jupyter Book to be launched on Ghub.

Note: the invoke script must have the executable file permission bits set. For example, use chmod 755 invoke to set the executable file permission bits.

### Create the New Tool on Ghub:

Follow the instructions on the https://theghub.org/tools/create web page to create a new tool. Select the Repository Host, Host GIT repository on Github. Select the Publishing Option, Jupyter Notebook.  

Note: created tools are launched from the Ghub Dashboard's My Tools component.

### Notes:

Current web browser results:

Firefox, Google Chrome, Microsoft Edge and Safari, Jupyter Book aligned properly, image displays and links work.<br>
