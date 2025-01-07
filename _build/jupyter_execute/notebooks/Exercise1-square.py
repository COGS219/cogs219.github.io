#!/usr/bin/env python
# coding: utf-8

# # Exercise 1 - Make a square and play with it

# Please [accept the first assignment](https://classroom.github.com/a/v93WIL47)
# 
# Once you clone the repository, you'll see a file with the starter code. This is the file you will edit and add to to complete the exercises. For reference, the code is reproduced below.
# 
# This starter code will show a blue square for half a second (500 ms) and then exit out of the program.

# In[1]:


import time
import sys
from psychopy import visual,event,core # import the bits of PsychoPy we'll need for this exercise

win = visual.Window([400,400],color="black", units='pix') #open a window
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100]) #create a Rectangle type object with certain parameters
square.draw() #draw the square to the screen buffer
win.flip() #make the buffer visible, i.e., show what's been drawn to it
core.wait(.5) #pause for half a second (i.e., 500 ms)
win.close() #close the window -- don't need this if you're running this as a separate file
core.quit() #quit out of the program -- don't need this if you're running this as a separate file


# **Go through each line of the code above and understand what each line does.**
# 
# Then spend the next 15 mins in class working through these parts. 
# 
# After each step, commit your solution to the Exercise 1 repository and **tag** it with the problem code, e.g., Exercise_1_1, Exercise_1_2, Exercise_1_3, etc. 
# 
# No need to rush. You'll finish the rest at home as your first assignment.
# 

# ## Exercise 1 parts
# 
# ```{note}
# Remember to tag each part with Exercise_1_1, Exercise_1_2 etc.
# ```
# 
# 1. Make the square red instead of blue
# 
# 2. Make the square appear for 1.5 secs.
# 
# 3. Show a red square for 1 second, then switch it to blue and show it for 1 second
# 
# 4. Show the following sequence: blue, red, blue, red, blue, red. Each color square should appear for 1 s with a 50 ms blank screen in the middle.
# 
#     ```{tip}
#     Use a list and loop through it! Do not copy/paste the same chunk of code multiple times.
#     ```
# 
# 5. Show a red square for 1 sec and then change its orientation by 45-deg
# 
#     ```{tip}
#     To change the orientation by a certain degree-value use square.setOri(value) where `value` is the new orientation.
#     ```
#     
# 6. Now make a square rotate continuously, one full revolution (360 degrees) per second
# 
#     ```{tip}
#     To increase orientation use `square.ori += value` where `value` is the value by which to increase the
#     orientation.
#     ```
# 7. Make a rotating square stop rotating when you press the 's' key
# 
#     ````{tip}
#     To accept keyboard input, use event.getKeys() and event.waitKeys(). Look at how these functions are defined at the [psychopy API web page](https://psychopy.org/api/event.html) or by typing `help(function name)`, e.g., `help(event.getKeys)` after importing `event`
#     ```{note}
#     getKeys checks if a certain key has been entered since the last call to getKeys, e.g., if an 's' was pressed, `event.getKeys(['s'])` will become True. event.waitKeys() waits until a certain key (or any key) was pressed. 
#     ```
#     ````
# 
# 8. Make a square stop rotating when you press 's' and then start rotating again when you press 'r'. Your code should keep running, rotating the square and stopping it whenever you press the `s` and `r` keys. Include a check for a `q` key which, when received, should quit the program.
# 
# 9. Display a blue square and increase its width (making it a rectangle) by 10 pixels whenever the user presses the left-arrow key. Decrease the width by 10 pixels when the user presses the right-arrow key
# 
#     ```{note}
#     The key codes for right and left arrows in PsychoPy are simply 'right' and 'left'
#    ```
# 
#     ```{note}
#     To change the width use `square.size += [x,y]` where `x` and `y` are the values by which you want to change
#     the size. x is the width; y is the height.
#     ```
# 
# 10. Show *two* rotating squares simultaneously, one left of center rotating clockwise, the other right of center, rotating counterclockwise. This is a little tricky. The squares should be visible at the same time and should not flash.
# 
# 11. Lastly, quickly [fill out this brief anonymous form](https://forms.gle/2vxSkbyViuBPSkzE8) that asks you how much time you spent on the assignment and what was most difficult. No need to do any commits for this part.
