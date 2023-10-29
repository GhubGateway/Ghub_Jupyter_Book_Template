## Ghub Jupyter Book Example

- Procedures and template files for hosting a Jupyter Book Github tool on the Ghub Science Gateway.<br>
- See https://theghub.org for more information on the Ghub Science Gateway.<br> 
- See https://help.hubzero.org/documentation/22/tooldevs/jupyter-notebooks for more information on Ghub Jupyter Notebooks.<br>
- See Jupyter Book Zenodo reference: https://doi.org/10.5281/zenodo.2561065 for more information on Jupyter Book.<br>

### Requirements:

#### notebooks directory

This directory contains the Jupyter Notebooks ending in .ipynb contained  by the Jupyter Book. 

#### jupyter_book_contents directory

This directory contains the Jupyter Book configuration file, _config.yml, and the Jupyter Book table of contents file, _toc.yml, as well as additional markdown files required to build the Jupyter Book including index.md and user_manual.md.

This directory also contains a link to the notebooks directory. Used ln -s ../notebooks notebooks to create the link. The name of the notebooks directory must be the same as the name of this directory specified in the jupyter_book_contents/_toc.yml file.

The name of the jupyter_books_contents directory must the same as the name of this directory specified in the src/Makefile and bin/showbook.sh files.

#### src directory

This directory contains the Makefile which contains the command to generate the Jupyter Book's HTML files on Ghub: jupyter-book build --all jupyter_book_contents. The generated HTML files are placed in the jupyter_book_contents/_build/html directory.

#### middleware directory

This directory contains the invoke script which enables the Jupyter Book to be launched on Ghub. When you create your tool on Ghub, please see the Create New Tool on Ghub section below, you will enter a name for your tool, for example ghubex2. The name of your tool should be the same as the name of your tool specfied in the middleware/invoke script's /usr/bin/invoke_app's -t option.

Note: the invoke script must have the executable file permission bits set. For example, use chmod 755 invoke to set the executable file permission bits.

#### bin directory

This directory contains the showbook.sh script to view the Jupyter Book's HTML files using a web browser.

Note: the showbook.sh script must have the executable file permissions bits set. For example, use chmod 755 showbook.sh to set the executable file permission bits.

### Create New Tool on Ghub:

Note: created tools are launched from the Ghub Dashboard's My Tools component.

Note: when a new tool is created you will receive an email with a link to the tool's status page. The tool's status page will allow you to let the Ghub administrators know when you are ready to install updates for your tool.

#### Host GIT repository on Github, Gitlab

Follow the instructions on the https://theghub.org/tools/create web page to create a new tool. Select the Repository Host: Host GIT repository on Github, Gitlab. Select the Publishing Option, Jupyter Notebook.  Enter the name of your tool, for example, ghubex2. The name of your tool should be the same as the name of your tool specfied in the middleware/invoke script's /usr/bin/invoke_app's -t option.

#### Host subversion repository on HUB

Alternately, follow the instructions on the https://theghub.org/tools/create web page to create a new tool and select the Repository Host: Host subversion repository on HUB. Select the Publishing Option, Jupyter Notebook and enter the name of your tool, for example, ghubex2.

In this case, the src/Makefile and middleware/invoke scripts will be created automatically and stored in the subversion repository (svn) on Ghub. You will need to modify the src/Makefile and middleware/invoke scripts and add the bin/showbook.sh script to the svn repository as required. You will also need to add the notebooks and jupyter_book_contents directories. The name of your tool should be the same as the name of your tool specfied in the middleware/invoke script's /usr/bin/invoke_app's -t option.

Example svn commands:

Enter svn checkout https://theghub.org/tools/ghubex2/svn/trunk ghubex2 to checkout files from the svn repository for your tool.<br />
Enter svn add <filename> to add files to the svn repository.<br />
Enter svn commit -m "commit message" to check updates into the svn repository.<br />

### Notes:

Current web browser results:

Firefox, Google Chrome, Microsoft Edge and Safari, Jupyter Book aligns properly, image displays and links work.<br>
