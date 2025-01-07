#!/usr/bin/env python
# coding: utf-8

# # Installation and setup for Windows
# 
# Python is not installed by default on Windows. We will be using the Anaconda environment which allows for easy installation of packages into a virtual environment which helps to eliminate software conflicts. 

# # Download CMDer
# 
# You will want to download and install [CDMer](https://cmder.app/). CMDer implements a mini BASH shell on your Windows machine and we'll use it to run various shell commands to give you experience with working in a shell. 
# 
# The CMDer page gives you the option to install CMDer Mini or CMDer full that includes `git`. If you already have git installed and want to continue to use it, feel free to install the mini version. If you don't have `git` installed, go ahead and install the full version. 
# 
# After it's installed you can click on the CMDer icon to start up the shell. If you installed the full version (with git), test that `git` works by typing 
# `git --version` at the shell (CMDer) prompt.
# 
# 

# # Install git
# If after the step above you still on't have git installed (🤔(, go ahead and [download and install](https://git-scm.com/downloads) the latest version of `git` 
# 
# Test it by typing 
# `git --version` 
# at the CMDer (shell) prompt.

# 
# # Install the Anaconda Distribution of Python
# * Download and Install the **Python 3.8 64 bit** [Miniconda installer](https://conda.io/miniconda.html). If you are asked whether you want the installer to prepend Anaconda to your PATH, respond ***yes***.
# 
# * Next let's create a virtual environment for this course. At the command prompt type
# 
# ```bash
# conda create -n psych750 python=3.8 pip
# ```
# 
# Once it's created, you can activate it by typing
# ```
# conda activate psych750
# ```
# 
# 
# ## Test the Anaconda Python install
# 
# Activate your environment using `conda activate psych750` and then type `python` to start the Python interpreter
# ```bash
# $ python 
# Python 3.8.13 (default, Mar 28 2022, 06:16:26)
# [Clang 12.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# ```
# 
# Now you can exit out of Python by typing:
# 
# ```bash
# exit()
# ```
# 

# 
# # Install the necessary Python packages
# 
# Now let's install the packages we'll need. Paste in the lines below, one at at a time, into your terminal -- not the Python interpreter. Make sure your new environment is activated first using `conda activate`. Wait for everything to install before proceeding to the next line.
# 
# ```bash
# conda install jupyter jupyterlab
# conda install pyaudio
# pip install psychopy
# ```
# 
# ```{note}
# Depending on your system, installing some of the packages that Psychopy requires may take quite a while (particularly the wxPython package which may need to be compiled). Be patient and let the install process run in the background.
# ```
# 
# ```{warning}
# If you run into any install errors, please **make note of the precise errors** and post them to the #installation_problems Slack channel.
# ```
# 
# ## Test PsychoPy
# 
# * Now let's test that `PsychoPy` installed correctly. Start the python interpreter and then import the psychopy package:
# 
# ```python
# >>> import psychopy
# >>> psychopy.__version__
# '2023.2.0'
# ```
# 
# If you see the verison number, the PsychoPy library probably installed correctly. But let's do some more tests.
# 
# * Let's test if PsychoPy can successfully open a new window.
# 
# Start the Python interpreter and type (copy/paste) the following:
# 
# ```python
# >>> from psychopy import visual
# >>> visual.Window((400,400),color="green")
# ```
# 
# When you hit enter after the second line, you should see a small green window appear. There may me some warnings displayed. You can safely ignore them.
# 
# ```{note}
# You won't be able to close the window like a regular window.
# Click on the terminal and enter `exit()` to quit the session and close the window.
# ```
# 
# * Finally let's test whether Psychopy can open pop-up boxes without issues
# 
# Copy/paste the following import statement into your Python interpreter:
# 
# ```python
# from psychopy import visual, gui
# ```
# 
# Now copy/paste this little function:
# 
# ```python
# def popup_box(text):
#     boxDlg = gui.Dlg(title="A pop up box", pos=(400,400))
#     boxDlg.addText('A pop up box: '+text, color='Red')
#     boxDlg.show()
# ```
# 
# And lastly, execute the function by calling it at the Python prompt like so:
# 
# ```python
# popup_box('Pop up test!')
# ```
# 
# If you saw a little pop-up window, all's good. If it doesn't immediately appear, check that it's not behind your active window. 
# 
# 
# There's a chance you might get the following error:
# 
# ```
# This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
# ```
# 
# If you do, you'll want to uninstall the pyqt6 package and install pyqt5 in its place. To do this, type the following commands into the CMDer terminal:
# 
# ```bash
# pip uninstall pyqt6
# pip install pyqt5
# ```
# 
# Now try it again beginning with 
# 
# ```python
# >>> from psychopy import visual, gui
# ```
# 
# ## Configure a few Psychopy settings
# 
# While we're here, let's also make sure the Psychopy settings are in order. Enter these lines in the python interpreter:
# ```python
# import psychopy
# psychopy.prefs.general['units']='pix'
# psychopy.prefs.hardware['audioLib'] = ['PTB', 'pyo','pygame']
# psychopy.prefs.saveUserPrefs()
# ```
# 

# # Let us know that Psychopy installed correctly
# 
# Let's double check that you're all set for class. Please download [this script](https://raw.githubusercontent.com/psych750/resources/main/installation_check/psychopy_validation.py) (if it opens in your browser, just save it to your hard-drive) and run it within your `psych750` environment by typing `python psychopy_validation.py` at the CMDer prompt. If you get errors, make sure you've followed all the instructions above prior to running the script. If you did and it still doesn't work, post on the #installation_problems Slack channel.
# 
# 
# ```{note}
# If you don't know how to save a file or run a file from a shell, please go back to [the prior to first class guide](https://psych750.github.io/notebooks/schedule.html#prior-to-first-class) and go through the basic shell command video/tutorial.
# ```

# 
# # Install Visual Studio Code
# 
# Visual Studio Code (often abbreviated as VS Code or VSC) is a very powerful and user-friendly code editor which we will use in this class to edit python/jupyter notebook scripts. Download Visual Studio Code [here](https://code.visualstudio.com) and install it.
# 
# Once installed, open up VS code and select File -> New Text File. At the top of the script, click select a language and select `python`. VS code will prompt you to install the Python extension. Once that is installed. Go back to your file and press `Ctrl + Shift + P`, and type in `Python: Select Interpreter`. Select the `psych750` python environment you created earlier. 
# 
# 
# ## Create a shortcut to Visual Studio code
# 
# It is very useful to be able to quickly access your editor from the shell.
# 
# VS Code installation on Windows automatically adds VS Code to $PATH. So you can type in the following in your Command Line:
# 
# ```bash
# code some_file_name.txt
# ```
# 
# where `some_file_name.txt` is the file you want to open. 
# 
# It should open up in visual Studio Code

# # Install R and RStudio Desktop
# 
# Next install R and RSudio Desktop by following the instructions [here](https://www.rstudio.com/products/rstudio/download/#download). Make sure to install Rtools as well when you download R.
# 
# ## Install a few R packages
# 
# Once R and RStudio are installed, make sure you can open up RStudio successfully and then install these packages (we may include some additional ones later).
# 
# At the RStudio prompt, type
# 
# ```r
# install.packages(c("tidyverse", "ggplot2", "lme4", "psych", "psychTools", "broom"))
# ```
# 

# # Download CMDer
# 
# You will want to download and install [CDMer](https://github.com/cmderdev/cmder/releases/). CMDer implements a mini BASH shell on your Windows machine and we'll use it to run various shell commands to give you experience with working in a shell. 
# 
# Extract all the files to your preferred location and run the `cmder.exe` software. Create a shortcut for it so you can access it easily.
# 
# ```{warning}
# CMDer developers recommend NOT extracting the files into C:\Program Files
# ```

# ## Adding R to Jupyter Notebook
# 
# It's handy to run R within jupyter notebook so you can have a markdown style document detailing what analyses and results you got. To install R and R kernel in jupyter, simply follow the steps below:
# 
# First you need to activate the psych750 environment in your CMDer:
# 
# ```bash
# conda activate psych750
# ```
# 
# Then enter the following command:
# ```bash
# conda install -c r r-irkernel
# ```
# 
# Once everything is installed, you can test it out by entering `jupyter notebook` in your CMDer window to start a new session. On the top right corner, select `new`, and it will prompt you to choose either the `python3` kernel or the `R` kernel.
# 
# You can also open these notebooks in Visual Studio Code. Open up an .ipynb file in Visual Studio Code, choose R as the Kernel and start running R code! The first time you do this, Visual Studio Code will prompt you to install some add-ons. Just click ok on the recommended extensions and you should be good to go.
