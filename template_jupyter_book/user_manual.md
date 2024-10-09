# User Manual

## Overview

This Jupyter Book tool provides a template and a guideline for you to create a Jupyter Book tool on Ghub.

Jupyter Book is an open-source tool for building publication-quality books and documents. We assume you are familiar with creating a Jupyter Book and with the structure of a Jupyter Book. See [Built with Jupyter Book](https://jupyterbook.org/en/stable/intro.html) and [Create a Template Book](https://jupyterbook.org/en/stable/start/create.html) for tutorials and more information on creating a Jupyter Book.   

On Ghub, the template's Makefile, showbook&#46;sh, and invoke scripts are required, to build Jupyter Books which enable the books' generated HTML files to display consistently across web browsers. This tool will guide you through the steps for creating a Jupyter Book tool on Ghub and incorporating these required files.

The template's Jupyter Book comprises this User Manual and two Jupyter Notebooks, notebook1.ipynb, which displays the template's directory tree, and notebook2.ipynb, which displays the content of select template files, including the required Makefile, showbook&#46;sh, and invoke scripts.

<a name="steps_to_create_a_jupyter_book_tool"></a>
## Steps to Create a Jupyter Book Tool

[Create Your Tool on Ghub](#create_your_tool_on_ghub)<br />
[Get the Template Files](#get_the_template_files)<br />
[Update Your Tool Using the Template Files as a Guideline](#update_your_tool)<br />
[Verify Your Tool's Updates](#verify_your_tool_updates)<br />
[Commit Your Tool's Updates to Your Tool's Repository](#commit_your_tool_updates)<br/>


<a id="create_your_tool_on_ghub"></a>
### Create Your Tool on Ghub[&#8607;](#steps_to_create_a_jupyter_book_tool)

- Follow the instructions on the [Create New Tool](https://theGhub.org/tools/create) web page.  Enter a name for your tool, referred to as **your_tool_name** in this document. Select the Publishing Option, Jupyter Notebook.<br><br> 
    
- When your tool is created with the **Host GIT repository on HUB** or **Host subversion repository on HUB** repository host, the tool's repository is automatically created using [Hub Tool Directory Structure](https://theghub.org/kb/development/directorystructure) guidelines. When your tool is created with the **Host GIT repository on Github, Gitlab, etc.** repository host, please follow the recommended directory structure for your GitHub repository. For a Jupyter Book tool, the src, bin, and middleware directories are required.<br><br>
    
- When your tool is created, you will receive an email with a link to the tool's status page. The tool's status page will allow you to let the Ghub Administrators know when you are ready to update, install, approve, or publish your tool. See [Tool development workflow](https://theghub.org/kb/development/tooldevelopmentworkflow) for more information on developing, testing, troubleshooting, and deploying tools on Ghub.


<a id="get_the_template_files"></a>
### Get the  Template Files[&#8607;](#steps_to_create_a_jupyter_book_tool)

- This tool's GitHub repository is located at [Ghub Jupyter Book Template](https://github.com/GhubGateway/Ghub_Jupyter_Book_Template) and can be cloned with: 
	- *git&#32;clone&#32;https&#58;&#47;&#47;github&#46;com&#47;GhubGateway&#47;Ghub&#95;Jupyter&#95;Book&#95;Template*.<br><br>


- In what follows, the name of the template's Jupyter Book is **template_jupyter_book** and the name of the subdirectory that contains the Jupyter Notebooks comprised by the template's Jupyter Book is **template_jupyter_book/template_jupyter_notebooks**.<br><br>

- The **template_jupyter_book** directory contains the Jupyter Book's configuration file, _config.yml, the Jupyter Book's table of contents file, _toc.yml, as well as additional files required to build the Jupyter Book including the index and user_manual markdown files. The **template_jupyter_book/template_jupyter_notebooks** subdirectory contains the notebook1.ipynb and notebook2.ipynb Jupyter Notebooks, and the _toc.yml file references these Jupyter Notebooks.<br><br>

- The template's src directory contains the required Makefile script, which contains the command to generate the Jupyter Book's HTML files on Ghub.<br><br>

- The template's bin directory contains the required showbook&#46;sh script, which contains commands to view the Jupyter Book's HTML files using a web browser.<br><br>

- The template's middleware directory contains the required invoke script, which contains the command to launch the Jupyter Book on Ghub.


<a id="update_your_tool"></a>
### Update Your Tool Using the Template Files as a Guideline[&#8607;](#steps_to_create_a_jupyter_book_tool)

- Launch the Workspace 10 Tool from the Ghub Dashboard's My Tools component, and in an xterm terminal window, git, svn, or clone the files from the **your_tool_name** repository.<br><br>

- In what follows, the name of your Jupyter Book is referred to as **your_jupyter_book** and the name of the subdirectory that contains the Jupyter Notebooks comprised by your Jupyter Book is referred to as **your_jupyter_notebooks**. Create the **your_jupyter_book** directory and the **your_jupyter_book/your_jupyter_notebooks** subdirectory. Copy and update files from the **template_jupyter_book** directory to the **your_jupyter_book** directory as required. Verify your tool's **your_jupyter_book/your_jupyter_notebooks** subdirectory contains the Jupyter Notebooks comprised by your Jupyter Book, and your tool's _toc.yml file references these Jupyter Notebooks.<br><br>

- Copy the template's Makefile script to your tool's src directory. Modify your tool's Makefile script and replace **template_jupyter_book** with **your_jupyter_book**.<br><br>

- Copy the template's showbook&#46;sh script to your tool's bin directory. Modify your tool's showbook&#46;sh script and replace **template_jupyter_book** with **your_jupyter_book**. The showbook&#46;sh script must have the executable file permissions bits set.<br><br>

- Copy the template's invoke script to your tool's middleware directory. Modify your tool's invoke script and replace -t **ghubex2** with -t **your_tool_name**. The invoke script must have the executable file permission bits set.


<a id="verify_your_tool_updates"></a>
### Verify Your Tool's Updates[&#8607;](#steps_to_create_a_jupyter_book_tool)

- For module testing only, the template's *jupyter_book_build_module_test.ipynb* Jupyter Notebook is provided.<br><br> 

- Copy the template's *jupyter_book_build_module_test.ipynb* to your tool's parent directory.<br><br>

- Launch the Jupyter Notebooks (202210) tool from the Ghub Dashboard's My Tools component, and open your tool's *jupyter_book_build_module_test.ipynb*.<br><br>

- Modify *jupyter_book_name* from **template_jupyter_book** to **your_jupyter_book**.<br><br>

- Modify *jupyter_book_notebooks* from **template_jupyter_notebooks** to **your_jupyter_notebooks**.<br><br>

- Select Kernel, Restart & Run All to build your Jupyter Book for module testing.


<a id="commit_your_tool_updates"></a>
### Commit Your Tool's Updates to Your Tool's Repository[&#8607;](#steps_to_create_a_jupyter_book_tool)

- When your tool is created with the **Host GIT repository on HUB** or **Host GIT repository on Github, Gitlab, etc.** repository host:

    - git add all new directories and all new or updated files
	- git commit -m "Your commit message"
	- git push<br><br>

- When your tool is created with the **Host subversion repository on HUB** repository host:

    - svn add all new directories and files
    - svn commit -m "Your commit message"<br><br>

- Go to your tool's status page and let the Ghub Administrators know that you have committed updates for your tool that are ready to be installed. A Ghub Administrator will build the Jupyter Book for your tool when your tool is installed.