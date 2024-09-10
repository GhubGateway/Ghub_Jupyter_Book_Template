# User Manual

## Overview

- This Jupyter Notebook tool provides a template for creating a Jupyter Book tool on Ghub.

- The template Jupyter Book comprises two simple Jupyter Notebooks, notebook1.ipynb, which displays the template's directory tree, and notebook2.ipynb, which displays the content of select template files. Click on a notebook's title to view the notebook's content.

## Create Your Jupyter Book Tool

### Get the Template Files

- This tool's GitHub repository is located at [Ghub Jupyter Book Template](https://github.com/GhubGateway/Ghub_Jupyter_Book_Template) and can be cloned with `git clone https://github.com/GhubGateway/Ghub_Jupyter_Book_Template`.

### Description of Files and Directories Provided by the Template Files

For this template, the name of the Jupyter Book is **template_jupyter_book**. The name of the directory containing the Jupyter Notebooks comprised by the Jupyter Book is **template_notebooks** . See [Create create a template book]( https://jupyterbook.org/en/stable/start/create.html) for more information on creating and naming Jupyter Books and on the structure of a Jupyter Book.

On Ghub, the template's ./src/Makefile, ./bin/show.sh and ./middleware/invoke scripts are required to build the Jupyter Book and enable the generated HTML files to display consistently across web browsers. A Ghub Administrator builds the Jupyter Book when the tool is installed. For unit testing, the test_jupyter_book_build.ipynb Jupyter Notebook is provided.

#### template_jupyter_book directory

- This directory contains the Jupyter Book's configuration file, _config.yml, the Jupyter Book's table of contents file, _toc.yml, as well as additional markdown files required to build the Jupyter Book. This directory also contains the **template_notebooks** directory, the _toc.yml file references files in the **template_notebooks** directory.

#### src directory

- This directory contains the Makefile script which contains the command to generate the Jupyter Book's HTML files on Ghub. The generated HTML files are placed in the **template_jupyter_book/_build/html** directory.

#### bin directory

- This directory contains the showbook shell script which contains commands to view the Jupyter Book's HTML files using a web browser.


#### middleware directory

- This directory contains the invoke script which contains the command to launch the Jupyter Book on Ghub.

### Create Your Tool On Ghub

- Follow the instructions on the [Create New Tool](https://theGhub.org/tools/create) web page.  Enter a name for your tool, referred to as **your_tool_name** in this document. Select the Publishing Option, Jupyter Notebook. 
    
- When your tool is created with the **Host GIT repository on HUB** or **Host subversion repository on HUB** Repository Host, the tool's repository is automatically created using [Hub Tool Directory Structure](https://theghub.org/kb/development/directorystructure) guidelines. When your tool is created with the **Host GIT repository on Github, Gitlab, etc.** Repository Host, please follow the recommended directory structure for your Git Repository.
    
- When your tool is created, you will receive an email with a link to the tool's status page. The tool's status page will allow you to let the Ghub Administrators know when you are ready to update, install, approve or publish your tool. See [Tool development workflow](https://theghub.org/kb/development/tooldevelopmentworkflow) for more information on developing, testing, troubleshooting, and deploying Tools on Ghub.


### Update Your Tool Using the Template Files as a Guideline

The name of your Jupyter Book is referred to as **your_jupyter_book** in this document. The name of the directory which contains the Jupyter Notebooks comprised by your Jupyter Book is referred to as **your_notebooks** in this document.

Launch the Workspace 10 Tool from the Ghub Dashboard's My Tools component and in a xterm terminal window, git, svn or clone the files from your tool's repository.

- Create the **your_tool_name**/**your_jupyter_book** and **your_tool_name**/**your_jupyter_book**/**your_notebooks** directories. Using the template files as a guideline, add / update files in these directories as required for your tool, verify your tool's _toc.yml file references files in the **your_notebooks** directory.

- Create the Makefile script required for your tool. Copy the template's ./src/Makefile script to your tool's src directory. Modify your tool's Makefile script, change **template_jupyter_book** to the name of your Jupyter Book.

- Create the showbook shell script required for your tool. Copy the template's ./bin/showbook.sh script to your tool's bin directory. Modify your tool's showbook shell script, change **template_jupyter_book** to the name of your Jupyter Book. The showbook shell script must have the executable file permissions bits set. For example, change mode (chmod) to 755.

- Create the invoke script required for your tool. Copy the template's ./middleware/invoke script to your tool's middleware directory. Modify your tool's invoke script, replace -t ghubex2 with -t **your_tool_name**. The invoke script must have the executable file permission bits set. For example, change mode (chmod) to 755.

- Verify your tool's updates. Copy the template's ./test_jupyter_book_build.ipynb to **your_tool_name/test_jupyter_book_build.ipynb**. Launch the Jupyter Notebooks (202210) tool from the Ghub Dashboard's My Tools component and open your tool's test_jupyter_book_build.ipynb. Modify jupyter_book_name to the name of your Jupyter Book. Enter Kernel Restart & Run All to build your Jupyter Book.

- Commit the your tool's updates to your tool's repository.

- Go to your tool's status page and let the Ghub Administrators know that you have committed updates for your tool that are ready to be installed.

## Learn About Software that Powers this Tool

See [Built with Jupyter Book](https://jupyterbook.org/en/stable/intro.html) for tutorials and more information on Jupyter Book.

See [Jupyter Notebooks Examples and Documentation](https://theghub.org/resources?alias=jupyterexamples) for more information on developing Jupyter Notebook tools on Ghub.




