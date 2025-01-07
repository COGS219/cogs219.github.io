#!/usr/bin/env python
# coding: utf-8

# # Exercise 5 - How well do you know everyone's names?
# 
# [Accept the exercise](https://classroom.github.com/a/p5G-KQFA)
# 
# This exercise will introduce you to some new features: We'll look at how we go about loading external files, we'll see how we deal with mouse clicks. Finally, we'll be continuing our quest to further modularize code by offloading common tasks -- those tasks not specific to this experiment -- to a separate function library. As a result our main code file will be much smaller and cleaner, containing only the code necessary for this specific experiment. 
# 
# Oh, and after you run yourself on this task, you'll be an expert in recognizing everyone in this class! (You may already be, but let's see how fast you are!).
# 
# ```{note}
# The names are being pulled from the official roster. If you'd like to use a different name for this exercise, send me a message on Slack and I'll update it. Since the names file is being automatically pulled from github, it will magically update in your code! If you'd like to use a different image, send me an image with the same dimensions as the ones in the stimuli folder and I'll update that too (those will *not* be automatically updated for everyone unless they re-pull the code from the exercise 5 starter repository)
# ```

# 
# On each trial, you will see a printed name of one of the students in the class. After a short delay you will then see a grid of your pictures (the ones from the course roster). You will then need to click on the picture of the named person as quickly as possible. You'll need to do some string manipulation to get the names in the right order and to figure out how to match the images to the name so that you can record whether the subject clicked on the correct image.
# 
# Notice the function library we've placed in your starter code repository (`my_first_function_library.py`). Use it! Import functions by typing `from my_first_function_library import X` where X is the function you'd like to import. Separate multiple functions with a comma just like we do when importing the various parts of psychopy. You can import all of them with  `from my_first_function_library import *` 
# 

# ## Part 1
# 
# Use `get_runtime_vars()` in the function library to get the runtime variables using a GUI box. Open the data file using `open_data_file()` which already has an error check built-in so you don't overwrite an existing data file. Also use the saving state trick I showed you to load in the previous values you used, so if you ran subject face_names_103, that's the value that should come up in the GUI box the next time you run the experiment. 
# 
# For the runtime variables, just use these:
# 
# * Subject code (subj_code)
# * Number of blocks (num_blocks -- an integer determining how many times we go through all the names. E.g., if num_blocks is 2, we go through all the names twice.
# 

# ## Part 2
# 
# Pass the runtime variables to generate_trials() so that it generates a subjCode_trials.csv trial file with the correct properties. This one's very simple -- just iterate through all the image files number of blocks times, in pseudo-random order (determined by the seed). The starter code for `generate_trials()` uses `os.glob()` to get a list of filenames inside the `stimuli` directory. Notice that the starter code for `generate_trials()` breaks up the fiename into its fields. Write these into appropriate columns in your trials file so that you can read them in and use them in your main script.
# 
# :::{tip}
# Add the following code to the bottom of `generate_trials.py`
# ```python
# if __name__=="__main__":
#     generate_trials({'subj_code':'test_subj1', 'number_of_blocks':1}, order=['subj_code', 'number_of_blocks'])
#     generate_trials({'subj_code':'test_subj2', 'number_of_blocks':2}, order=['subj_code', 'number_of_blocks'])
#     generate_trials({'subj_code':'test_subj3', 'number_of_blocks':3}, order=['subj_code', 'number_of_blocks'])
# ```
# This should generate 3 test files. Look at them to make sure that they have 1, 2, and 3 blocks, respectively.
# :::
# 
# ```{admonition} Extra credit! (1pt)
# Add a `seed` runtime variable which controls the order of trials using `random.seed(seed)`. You know it's working if several trial lists generated with the same random seed have the very same random order of trials. Tag it as `Exercise_5_seed`
# ```
# 
# You trials .csv file should have the runtime variables and the trial variables (name you're being asked about, name of the image file corresponding to the correct answer). Make sure your trial file has column headers.
# 
# 

# ## Part 3
# 
# Read in the trial file -- use column headers! --  show the appropriate trial, and implement `compute_accuracy()` and `present_feedback()` functions. These are currently placeholders.
# 
# compute_accuracy should return a 1 if the subject clicked on the correct name and a 0 otherwise.
# Note that the hard work is already done by this function-call
# 
# ```python
# def which_image_clicked(coord,pics):
#     clicked_images =[]
#     for pic_name,image in pics.items():
#         if image.contains(coord):
#             clicked_images.append(pic_name)
#     if len(clicked_images)>1:
#         raise Exception("Looks like you have overlapping images and you clicked on an overlap! Boo! Returning 1st one")
#     return clicked_images[0]
# 
# image_clicked = which_image_clicked(coord,pics)
# ```
# 
# ...all you need to do when implementing `compute_accuracy()` is to check if the name string matches the filename
# 
# 
# For present_feedback(), use the output of compute_accuracy to show a red X or green check-mark depending on whether the subject responded correctly or not.
# 
# 
# ```{admonition} Extra credit! (1pt)
# Read in buzz.wav and bleep.wav inside the /sounds directory and play a bleep after a correct response and a buzz after an incorrect response. Tag it as `Exercise_5_sounds`
# ```
# 

# ## Part 4
# 
# Write the trial information and response to a data-file: subj_code_data.csv placed inside a data subfolder. The data-file should be in the following format. *Please make sure your format is exactly this -- these columns in this order, separated by commas* Make sure your output file has at least one full block of trials.
# 
# ```
# Col 1: subject_code
# Col 2: trial_number (beginning with 1)
# Col 3: number_of_blocks
# Col 4: current block number beginning with 1
# Col 5: prompted name (e.g., Gary Lupyan)
# Col 6: filename of the shown image, e.g., gary_lupyan.png
# Col 7: name of the person whose image was clicked on
# Col 8: the x coordinate of the click
# Col 9: the y coordinate of the click
# Col 10: is_correct - 1 if the subject clicked on the correct image (i.e., of the person in col 7), 0 otherwise
# Col 11: RT - reaction time from onset of all the images, to subject's response, in milliseconds, rounded to the nearest millisecond
# ```
# 
# The first line of your file should be the column names, i.e,
# 
# ```
# subj_code,trial_num,number_of_blocks,current_block_num,name_prompt,photo_filename,clicked_image,click_x,click_y,is_correct,RT
# ```
# 
