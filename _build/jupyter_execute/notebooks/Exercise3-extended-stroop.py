#!/usr/bin/env python
# coding: utf-8

# # Exercise 3: Extending the Stroop effect
# 
# [Accept the exercise](https://classroom.github.com/a/ecZMU1tX).
# 
# In this exercise we'll be extending the Stroop effect task you coded for Exercise 2 into a more complete experiment that (1) generates stimulus lists that are then read in by the main script, (2) accept runtime variables to assign participants to conditions and record participant codes, and (3) use some out-of-the-box speech recognition to allow participants to respond by using their voice.
# 
# We'll use the all same stimuli, but introduce several variations: 
# 
# a. We'll vary the proportion of trials that are incongruent (i.e., when the color of the font does not match the word). Make sure you go through the [randomization notebook](https://psych750.github.io/notebooks/trial_generation.html) first!
# 
# b. We'll introduce an orientation manipulation so that on 50% of trials the word is presented upside down (what effect do you think this will have on response times?)
# 
# c. The output will now be written to a results file (teaching you file access in the process).
# 
# In this exercise we'll also start modularizing the code so that one part of it is responsible for generating the trials, another for reading in the trial list, another for showing the stimuli, and another for writing the participant's responses to a file. This is preparation for coding larger projects.
# 

# ## Exercise 3 parts

# ## Part 1.
# Complete the `generate_trials()` function below so that it writes a file with all the trials to be presented to the participant.

# In[9]:


def generate_trials(subj_code, prop_incongruent, num_trials=100):
    '''
    Writes a file named {subj_code_}trials.csv, one line per trial. Creates a trials subdirectory if one does not exist
    subj_code: a string corresponding to a participant's unique subject code
    prop_incongruent: float [0-1] corresponding to the proportion of trials that are incongruent
    num_trials: integer specifying total number of trials (default 100)
    '''
    import os
    import random
    
    try:
        os.mkdir('trials')
    except FileExistsError:
        print('Trials directory exists; proceeding to open file')
    f= open(f"trials/{subj_code}_trials.csv","w")
    
    pass


# :::{tip}
# The text at the start of the function explaining what it does and its arguments is called a ["docstring"](https://classroom.github.com/classrooms/110263119-psych750-fa22). This is the proper way to document what a function does. Unlike comments, which are completely ignored by the Python interpreter, docstrings are part of the function and can be accessed like so: `print(generateTrials.__doc__)`. 
# :::
# 
# The produced file should be a CSV and have the following format:
# 
# Col 1: subject code
# 
# Col 2: proportion of incongruent trials
# 
# Col 3: the word to be shown
# 
# Col 4: the color of the word
# 
# Col 5: whether the trial is 'congruent' or 'incongruent'
# 
# Col 6: The orientation of the word, "upright", or "upside_down". Please ensure that 50% of the congruent trials are upright (and the remaining are upside-down). Same thing for incongruent trials -- 50% should be upright and the remainder upside-down. What this means is that if there are 100 total trials and 25% are incongruent, then 75/2 of the congruent trials (rounded to the nearest integer = 38) should be upright and 25/2 of the incongruent trials (rounded = 13 trials) should be upright.
# 
# 
# Make sure the trial order is **randomized** (i.e., shuffle the order) so that you don't have all the congruent trials together, all the trials containg the same word together, etc.
# 
# 

# ## Part 2
# 
# Extend the script you wrote for Exercise 2 (or use the provided solution if you like) to accept these 2 runtime variables [using a GUI box](https://psych750.github.io/notebooks/Psychopy_reference.html#a-simple-function-for-popping-up-an-error-using-a-gui-window):
# 
# - subject code (any string, but conventionally something like stroop_101, stroop_102, etc.)
# - proportion of incongruent trials (drop down box of 25%, 50%, and 75%)
# 
# The entered values should be stored in a dictionary called `runtime_vars`. After the values are collected, the dictionary might look like this:
# 
# ```python
# runtime_vars= {'subj_code':'stroop_101', 'prop_incongruent':25}
# ```
# 
# ```{note}
# This dictionary must be populated dynamically. You should not be hard-coding any of these values
# ``` 
# 

# ## Part 3
# 
# Extend the script further to read in the trials data-file. Once its read in, step through the file, one trial (i.e., line) at a time & show the appropriate stimuli. For example, if trial 3 in the trial file shows the word "green" in red font in an upside-down orientation, then that's what your experiments should be doing on trial 3.

# ## Part 4
# 
# Define a `write_data()` function in your code that is called after every response and writes all the trial information **and** responses to a file. 
# 
# You should be writing to the file after every trial (not at the very end). Make sure your data is written to `data/subject-code_data.csv` where `subject-code` is the subject code entered at runtime and `data/` is a subdirectory that will contain all the data files. Your code should record one line per response and record responses as they come in. If a user quits after trial 50, the data file should have recorded those 50 responses.  Here's an example of what your output file should look like (note that the first line contains column name).
# 
# | subj_code  | trial_num | prop_incongruent | word   | color | congruence  | orientation | resp | is_correct | RT  |
# |------------|-----------|------------------|--------|-------|-------------|-------------|------|------------|-----|
# | stroop_101 | 1         | .5               | green  | blue  | incongruent | upright     | b    | 1          | 898 |
# | stroop_101 | 2         | .5               | green  | green | congruent   | upright     | g    | 1          | 754 |
# | stroop_101 | 3         | .5               | yellow | red   | incongruent | upside_down | y    | 0          | 902 |
# 
# ```{note}
# Use a CSV format as before: fields are separated by commas
# ```  
# 
# ```{admonition} Challenge!
# Ensure that you can't run the same participant code twice. If you enter a participant code that's already been entered before, PsychoPy should pop-up a warning box saying "Participant code already exists". This should prevent you from overwriting an existing data-file. If you take up this challenge, tag it as e3_4_challenge
# ```
