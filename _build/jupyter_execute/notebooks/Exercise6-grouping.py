#!/usr/bin/env python
# coding: utf-8

# # Exercise 5: A perceptual grouping task
# 
# In this task we will be building on the skills you've acquired so far with lists, dictionaries, and trial generation to build a fuller experiment that tests the strengt of perceptual grouping by color and by shape.

# Here is some "bad" code that shows a small blue circle and a blue square. We will be improving and expanding this code to build a full-blown experiment.

# In[ ]:


from psychopy import visual, core, event
import random
 
win = visual.Window([800,600],color="black", units='pix')
 
circle = visual.Circle(win,size = 20)
square = visual.Rect(win,size = 40)
locations = [[-15,0], [15,0]]
colors = ['blue', 'blue']
 
circle.setPos(locations[0])
circle.setFillColor(colors[0])
circle.setLineColor(colors[0])
circle.draw()

square.setPos(locations[1])
square.setFillColor(colors[1])
square.setLineColor(colors[1])
square.draw()

win.flip()

event.waitKeys('q')
win.close()
core.quit()


# -   For the next 15 minutes, see if you can figure out how adapt the code above to
#     display an arbitrary number of alternating circles and squares that look like
#     the image below (shown on a black background). We'll be doing a lot
#     with this code. Make it as extendable as possible. For example, the
#     spacing and the number of items should be easily changeable. Your
#     code to generate the series of alternating images needs to be
#     *shorter* than the base code above.
# 
# ![Alternating shapes](images/alternatingShapes.png)
# 
# 1.  Now, for each trial, pick a random shape and "flip" it such that
#     you have two squares or two circles in a row. The colors should
#     always alternate. So, you might have a red-square, blue-circle,
#     red-circle, blue-square , etc.(a repetition of two circles in a
#     row). Note, you will need to do more than just flip the one shape to
#     make this work (flipping a single shape in an alternating sequence
#     will create a sequence of three repeated items, which is not what
#     you want).
#     
#     <div class="alert alert-block alert-info">
#     **Hint:** random.choice([0,1]) will output 0 or 1. The items in the list supplied as the argument to the random.choice function can be anything, e.g., random.choice(['within','between']) will output the words 'within' or 'between' randomly.
# </div>
# 
# 2.  Make it so that 50% of the trials have a shape repeat and 50% don't. Here's an example of a repeated-shape trial
#     ![Repeated shape](images/repeatedShape.png)    
# 
# 3.The subject's task is to detect the repetition. If there's a
#     repetition, they should press the 'up' arrow. If not, the 'down'
#     arrow.
#     
# 4.Let's extend the task to also have repeated colors instead of just repeated shapes. We should now have 50% no-repeats, 25% repeated colors, and 25% repeated shapes. Here is an example of a repeat color trial:
#     ![Repeated color](images/repeatedColor.png)    
# 
#     
# 5.Now let's add some feedback. If there's an error, and only if there's
#     an error, display the word 'ERROR' in red after the response.
# 
# 6.Now let's make the subject report what shape was repeating. Make it so
#     that if they press the 'up' arrow, they then see a prompt
#     "Repeated square or circle?" which should stay up until they
#     respond with the 's' key for square and the 'c' key for circle.
#     If they press the 'down' arrow, just go on to the next trial.
# 
# 7.Now, let's actually keep track of how people are responding! For
#     each trial, output the variables listed below to a file called
#     results.txt. You can use the following code to create a line in which each variable is separated by a tab, and then write that line to your output file. Your final experiment should have 100 trials.
# 
# ```Python
# '\t'.join([string1, string2, string3, stringN])
# ```
# <div class="alert alert-block alert-info">
# Remember that each item in the list passed to join must be a string, so any items that are not (hint: the Reaction Time) must be first converted to a string using str(RT).
# </div>
# 
# <div class="alert alert-block alert-info">
# Is there a better way to convert a bunch of possibly non-string variables to a string? Sure! Try map(str, (var1,var2,var3)) or [str(var) for var in (var1,var2,var3)]</div>
# 
# 
# See [how to write to a file safely](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Python_reference.html#Writing-to-a-file,-safely)
# for instructions on writing to a file one line at a time, making sure that there is no data loss if your program crashes. The output for each trial should contain:
#     -   The number of the trial (1, 2, 3 etc.)
#     -   The correct response (repeat, noRepeat)
#     -   Position of the repeated stimulus, e.g., if the 4th and 5th elements
#         are the shame shape, output 4. If there's no repeat, output 'NA'
#     -   Whether the repeating shape is a circle or a square (i.e., output
#         the words 'circle' or 'square' or NA if this is a noRepeat
#         trial)
#     -   The subject's responses (note that there are two: the first is
#         whether there's a repeat. The second is what the repeat is)
#     -   Correctness of the first response, correctness of the second
#         response (1 for correct, 0 for incorrect)
#     -   The response times for both responses in milliseconds
# 8.This file will contain their responses and trial parameters, but we don't know who the subject is! Remember when I had you pop up a box to enter in a person's name? Do the same thing here, but pop up a box to ask for the subject code. Now that you have subject code stored in a variable, what should you do with it? Two things. First, use it to name your file. Instead of a generic "data.txt", you'll want to have separate data files for each subject. So let's use the subject code as the filename! Second, let's include it in the output file. Because we'll be concatenating the files for later analysis, let's include the subject code as the first column of your output file. 
# 
# <div class="alert alert-block alert-info">
# What should the subject codes be? I strongly suggest using a unique experiment identifier followed by a sequential number, e.g., repetition_101, repetition_102, etc. (there's a good reason to start with 100 instead of 1. Can you figure out what it is?)</div>
# 
# ***As part of your submission for this exercise, I would like you to run through at least 50 trials of the experiment as though you were a subject. If everyone follows the specifications above, I should be able to concatenate your output files and immediately graph the results and run analyses.***
# 
# 

# **Bonus**: instead of having people respond with circle/square, let's
# make them tell us exactly where the repetition was. After they make a
# repeat/no-Repeat response, have the shapes change to X's and have the
# subject indicate with the mouse (ooo!) where the repeat was. Mark it as
# correct or not. If you want to try a 'bonus-lite' version, change the
# shapes to letters: a,b,c,d,e,f,g,h,i,j,k,l,m,n,o and have the subject
# press the letter corresponding to where the repeat was.

# In[ ]:




