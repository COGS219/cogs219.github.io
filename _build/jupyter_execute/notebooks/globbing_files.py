#!/usr/bin/env python
# coding: utf-8

# # Preloading files
# 
# It is generally a good idea to load your external stimuli (images, movies, sounds) into memory prior to presenting them. This helps ensure greater precision in display times. (One exception is if you are loading many 1000s of images in which case you may want to preload them in batches -- this won't be an issue for us).   
# 
# One effective approach is to have all your stimuli in one directory (e.g., `stimuli`) and then just load all the files in that directory into memory at the start of the experiment. The trick is to load them in a way that allows you easy access.
# 

# In[2]:


import os
import glob


# First, a few useful functions for managing directories and file paths. For more info, see `help(os.path)`

# In[2]:


import os

print(os.getcwd()) #what's my current directory?
try:
    os.mkdir('data') #make a new subdirectory called data. If it already exists, raise a `FileExistsError`` 
except FileExistsError:
    print('already exists')
os.path.exists('data') #check if a path (a directory or filename) exists
print(os.path.join(os.getcwd(), 'stimuli/visual/')) #creating a longer path
os.path.basename('/stimuli/visual/lamp.jpg') # get just the filename part of a path


# ## Grabbing (globbing) all the files in a directory
# 
# With these preliminaries out of the way, we can now combine them with `os.glob()`
# First, please [clone this repository](https://github.com/psych750/activity_debugging_experiments).
# 
# Now `cd` into it. Inside will be a copy of this notebook. Open it inside VSCode. This will ensure that the current working directory is the new repository.

# The code below grabs all the files that meet your criteria Confused by the '*' syntax? Those are wildcards -- a key part of navigating around a file system -- [see more here](https://linuxhint.com/bash_wildcard_tutorial/) if you need a refresher.

# In[53]:


import os
import glob

all_pics = glob.glob('images/*png')
print(all_pics[0:10]) # printing just the first 10 for brevity


# In[52]:


pics_beginning_with_a = glob.glob('images/a*png')
print(pics_beginning_with_a)


# Now let's get just the filename part of the path

# In[10]:


just_names = [os.path.basename(file) for file in all_pics]
print(just_names)


# ## Preloading images into memory
# 
# Now that we've seen how to grab a list of files, let's use this to preload them into memory and then access the psychopy objects we've created. Below is a basic version of a useful helper function `load_files()` that does just that. A more flexible version with some bells and whistles (e.g., it works for both images and audio files) is available [here](https://psych750.github.io/notebooks/Psychopy_reference.html#preloading-image-and-audio-files).

# In[48]:


import os
import glob
from psychopy import visual

def basic_load_files(directory,extension,win='',restriction='*'):
    """ Loads all the pictures (or narrowed by the restriction argumnt) in the provided directory.
    Need to pass in the Psychopy window (win) object so that it can be used for loading them in.
    Returns a dictionary with references to the loaded images
    """
    file_list = glob.glob(os.path.join(directory,restriction+extension))
    images = {} #initialize fileMatrix  as a dict because it'll be accessed by file names (picture names, sound names)
    for cur_file in file_list:
        stim_filename = os.path.splitext(os.path.basename(cur_file))[0] #just the filename without the extension
        stim = visual.ImageStim(win, image=cur_file,mask=None,interpolate=True)
        images[stim_filename] = stim
 
    return images

win = visual.Window([200,200],color="black", units='pix')
images = basic_load_files('images/','png',win=win)


# Now to show an image, we can simply use the returned dictionary!

# In[50]:


print(type(images['duck'])) # notice the type
images['duck'].draw()

