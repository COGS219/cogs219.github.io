#!/usr/bin/env python
# coding: utf-8

# # Basic Linux commands
# 
# 
# ## Listing files, changing directories, and making new directories
# 
# Find out what directory you're currently in
# 
# ```bash
# pwd
# ```
# 
# Go to your home directory
# 
# ```bash
# cd ~
# ```
# 
# Make a new subdirectory called data
# 
# ```bash
# mkdir data
# ```
# 
# Now go into the directory
# 
# ```bash
# cd data
# ```
# 
# Now go back to the directory above it
# 
# ```bash
# cd ..
# ```
# 
# List the files in your home directory
# 
# ```bash
# ls ~
# ```
# 
# List the files in the current directory with a bunch of extra information
# 
# ```bash
# ls -l
# ```
# 
# List just the names of the files, in a single column, with no extra information.
# 
# ```bash
# ls -A1
# ```
# 
# List just the text files, single column, no extra info, and store the list in a file called myTextFiles.txt
# 
# ```bash
# ls -A1 *txt > myTextFiles.txt
# ```
# 
# Display a list of files sorted by date, with the most recent first
# 
# ```bash
# ls -lt
# ```
# 
# Display a list of files sorted by date, with the oldest first
# 
# ```bash
# ls -ltr
# ```
# 
# ```{tip}
# Those letters that specify options after linux commands are called command flags
# ```

# ## Copy/move/delete files
# 
# Copy all the files whose filename contains the word *data* into the data directory
# 
# ```bash
# cp *data* data
# ```
# 
# *Move* all the files whose filename contains the word *data* into the data directory.
# 
# ```bash
# mv *data* data
# ```
# 
# *Delete* all the files containing the word *data* in the current
# directory. (**Be careful with this! These files get deleted,
# bypassing the Trash/Recycle-bin**)
# 
# ```bash
# rm *data*
# ```

# ## Rename files
# 
# Simple renaming of a file
# 
# ```bash
# mv crappyFilename.png usefulFilename.png
# ```
# 
# More complicated renaming of a file - prefix a string to a filename:
# Grab a list of all the files with the extension .png and then
# prefixing "mask\_" to each one
# 
# ```bash
# for filename in *.png; do mv "$filename" "mask_$filename"; done;
# ```
# 
# More complicated renaming of a file - replace a part of all filenames with something else
# 
# ```bash
# for filename in *.png*; do mv "$filename" "${filename//maskSquare/maskCircle}"; done
# ```

# ## Display a file
# 
# Print a history of your commands to the screen
# 
# ```bash
# cat ~/.bash_history
# ```
# 
# One screen at a time...
# 
# ```bash
# cat ~/.bashrc | more
# ```
# 
# Just the top
# 
# ```bash
# head ~/.bashrc
# ```
# 
# Just the bottom
# 
# ```bash
# tail ~/.bashrc
# ```
# 
# The first 10 lines
# 
# ```bash
# head -n 10 ~/.bashrc
# ```

# ## Combine (concatenate) two or more files and write the output to another file
# 
# ### Combine two files and print the results to the screen
# 
# ```bash
# cat file1.txt file2.txt
# ```
# 
# (conCATenate, get it?)
# 
# ### Combine all files with the word 'data' in the filename and which end on txt.
# 
# ```bash
# cat *data*txt
# ```
# 
# ### Do the same and write the output to a new file
# 
# ```bash
# cat *data* > allDat.txt
# ```
# 
# (if allDat.txt already exists, it will be overwritten) Caveat: what
# happens if you try `cat *data* > alldata.txt`
# 
# ### **Append** the output to a file (i.e., add to the end of the file)
# 
# ```bash
# cat *data* >> allData.txt
# ```
# 
# ### Concatenate files while getting rid of the first line
# 
# If you want to concatenate files that contain a column header, combining them using `cat` will cause your resulting file to have lots of headers instead of just 1, at the top. There's an easy (though unintuitive) solution for it: use `tail` with some options to print all but the first line.
# 
# ```bash
# tail -n +2 file1.txt
# ```
# 
# You can direct it to output using `>` as with cat (or any bash command). To combine multiple files, add them as above, e.g.
# 
# ```bash
# tail -n +2 *data*txt > allDat.txt
# ```
# 
# You'll notice that if you pass multiple files to `tail`, it will print the filename at the start of every file. This will mess up your neatly formatted file. To suppress the filename add `-q`, i.e.,
# 
# ```bash
# tail -q -n +2 *data*txt > allDat.txt
# ```
# 
# ### Use cat and tail together: 
# 
# Let's say you want to concatenate all of one file and all but the first line of other files. You can chain `cat` and `tail` like this:
# 
# ```bash
# cat files_whose_header_you_want_to_keep*txt && tail -q -n +2 files_whose_header_you_want_to_omit*txt > allDat.txt
# ```
# 
# ```{note}
# Make sure all your files end with a newline or the first line of the next file will continue from the last line of the previous file.
# ```
# 

# # Some miscellanous tips
# 
# ## Get help on a command
# 
# To look up detailed specifications on a command, type:
# 
# ```bash
# man ls
# ```
# 
# ```{note}
# If you're using Cmder on windows, man won't work. Use `ls --help | less` instead
# ```
# 
# You can scroll through the documentation using PgUp/PgDown or up and
# down arrows. To exit, press `q`
# 
# For a quick refresher on the arguments
# 
# ```bash
# ls --help
# ```
# 
# There are many many many linux commands. Probably the best way to find one is
# by Googling, e.g., google for `how to zip a file in linux` or `ls command flags`
# 
# You can also try the `apropos` command in the terminal. For example, try
# 
# ```bash
# apropos zip
# ```

# ## Become a more proficient computer user
# 
# - Use command-tab (Mac), alt-tab (windows) to switch between programs.
# - Learn keyboard shortcuts: shortcuts for Cut, Copy, Past, Select-All,
#   Find, undo/redo, should be second nature. Here's a [list of Mac shortcuts](https://support.apple.com/en-us/HT201236), and a list of [Windows shortcuts](https://support.microsoft.com/en-us/kb/126449).

# ## Navigating a command line efficiently
# 
# You can cycle through previous commands using the up/down arrows.
# Unlike a graphical text editor, you can't mouse-click on a
# particular spot in a command line. For short commands, you can just
# use the left and right arrows to move the text insertion point in a
# command line. The following keyboard shortcuts are handy for
# navigating around longer command lines:
# 
# - **Ctrl-a** moves to the start of the command
# - **Ctrl-e** moves to the end of the command
# 
# You can also use the 'Home' and 'End' keys! (perhaps the most underused keys on a keyboard)
# 
# - **Esc-b** (i.e., the Escape key followed by the b key) moves back one word
# - **Esc-f** moves forward one word
# - **Ctrl-k** will cut the command line from the cursor point forward and place it in a buffer (aka clipboard)
# - **Ctrl-y** will paste what is in the buffer after the current cursor position
# 
# ### Use tab completion
# 
# Type `cd` then a space then the first letter or two of the directory you
# want to go to. Press <tab>.  Magic.
# 
# Caveat: commands like `ls` and `cd` are little executable programs. The
# stuff that follows the command is an argument (information telling the
# program what you want it to do). As with all programs, you must put a
# space in between the program name and its arguments, so it's
# `ls --help`, *not* `ls--help`.
# 
# If you're using cygwin (linux shell for Windows), try this at the
# prompt:
# 
# `explorer .`

# ### Count words/lines/characters in a file
# 
# ```bash
# wc ~/.bash_history
# ```
# 
# Display the number of lines for all the text files in the current directory
# 
# ```bash
# find . -name "*txt" -exec wc -l {} \;
# ```

# ### Get a particular column from a file
# 
# There are many ways to do this, but the simplest is:
# 
# ```bash
# cut -f1 test.txt
# ```
# 
# This gets the first column from a file called test.txt which has several
# columns separated by a tab (`cut` defaults to a tab delimiter. You can
# specify your own with `-d "delim"`
# 
# A more powerful way of selecting particular columns is using awk.
# See if you can figure out how this works:
# 
# ```bash
# ls -l | awk '{print $6,$7,$8}'
# ```
# 
# How would you use awk to get a list of word-counts for all the .txt
# files in your directory?

# ### Send an output of one command to another command
# 
# You do this using the pipe operator '|' (so *that's* what that key is!)
# 
# For example, the grep command in its basic form searches through text
# and outputs a line that matches some search term. Recall that you
# created an alias for psych750 in your .bashrc file. Let\'s find it.
# 
# ```bash
# cat ~/.bashrc | grep psych750
# ```
# 
# This means send the output of `cat ~/.bashrc` (the contents of the
# .bashrc file) to the command `grep` which then tries to find
# "psych750" within that output.
# 
# ```{note}
# You can also just type `grep "psych750" ~/.bashrc`, but in some
# cases using the pipe (`|`) is the only way to do what you need to do.
# ```

# In[ ]:




