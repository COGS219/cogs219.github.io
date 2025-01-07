#!/usr/bin/env python
# coding: utf-8

# # Exercise 3: Trial generation 1
# 
# 
# In this exercise we will begin to develop the skills needed to generate trial lists which, when generated properly, can be read in by your main experiment script and will provide it with instructions of what to show on each experimental trial, what the expected responses are, etc. 

# ## Repetition
# 1.  Write a function called *repetition* which takes three arguments: *letters* (a list), *numberBeforeSwitch* (an integer), and *numRepetitions* (also an integer). The function should produce a sequences of letters, one per line, such that calls to *repetition* with various parameters, generate the following outputs. (Note: There are built in functions that can do this. Please do not use them for the exercise).

# ```Python
# >>> repetition(['A','B'],1,1)
# A
# B
# 
# >>> repetition(['A','B'],2,1)
# A
# A
# B
# B
# 
# >>> repetition(['A','B'],2,2)
# A
# A
# B
# B
# A
# A
# B
# B
# 
# >>> repetition(['A','B','C'],3,1)
# A
# A
# A
# B
# B
# B
# C
# C
# C
# ```
# 
# Inside your repo you will find repetition.py which contains the following starting code:

# In[3]:


def repetition(letters,numberBeforeSwitch,numRepetitions):
    pass


# Remember, your function should print one letter per line.

# ## Generating a simple trial list. 
# 
# 
# Ok, now for something more useful. 
# 
# Suppose we are interested in finding out the efficacy of a particular kind of masking technique and want to examine if it's more effective in the left vs. right visual field. Let's code a basic trial list for an experiment in which we display an image on either the left or the right side of the screen. Both sides of the screen are then masked, and we are interested in measuring people's ability (e.g., accuracy, reaction time) in responding whether the image was on the right or left side of the screen, while comparing responses on masked vs. nonmasked trials. 
# 
# To do this, we need to generate a list of trials in which some proportion is masked and some is not masked. Within each condition, we want the image on the left side displayed with some proportion of the time, and on the right the remaining times. 
# 
# Let's begin by having 2/3 masked trials and 1/3 non-masked trials. Within each level of the masking factor, half of the targets should be on the left and half on the right. Let's have 5 blocks with each block having all the possible trial types. 
# 
# The code you write should output to the terminal output that looks just like this (that first number is the block number).
# 
# ```Text
# $ python generateTrials.py
# 1,masked,right
# 1,masked,left
# 1,masked,right
# 1,masked,left
# 1,nonmasked,right
# 1,nonmasked,left
# 2,masked,right
# 2,masked,left
# 2,masked,right
# 2,masked,left
# 2,nonmasked,right
# 2,nonmasked,left
# 3,masked,right
# 3,masked,left
# 3,masked,right
# 3,masked,left
# 3,nonmasked,right
# 3,nonmasked,left
# 4,masked,right
# 4,masked,left
# 4,masked,right
# 4,masked,left
# 4,nonmasked,right
# 4,nonmasked,left
# 5,masked,right
# 5,masked,left
# 5,masked,right
# 5,masked,left
# 5,nonmasked,right
# 5,nonmasked,left
# ```

# <div class="alert alert-block alert-info">
# Try redirecting the output from the screen, to a file using `>`. At the terminal, type `python generateTrials.py > trialList.txt`. Now open up the trialList.txt file and your trial list should be right there.
# </div>

# ## Randomizing
# 3 - The trial list above has the trial structure you want, but obviously you wouldn't want to show someone trials in this order because it's completely predictable. It's a good idea to have your `generate trials` routine do all the randomization ahead of time such that your trials file (here, trialList.txt) contains the exact trial order that will be seen by a participant. There are two reasons. First, this lets you modularize all the trial handling outside of your main experiment script. Second, it allows you to save individual trial files that show the trial order seen by a given participant. It comes in handy for making sure your trial list is set up as you want it. So: let's go ahead and *randomize the trial list before printing.* 

# ## Randomizing within blocks
# 4 - Simply randomizing the enture list messes up the block structure creating the possibility that participants will see the same trial multiple times in a row. For this part, randomize the trials *within* each block before printing the list.

# ## Extending each block
# 5 - Double the number of trials in each block (so that the repetitions are not quite so predictable), and then randomize within each block as in part 4.
