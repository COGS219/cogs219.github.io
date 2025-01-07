#!/usr/bin/env python
# coding: utf-8

# # Exercise 5 - Categorizing Facial Expressions

# ## Modularize generateTrials
# Now that you have a working version of the basic expression-categorization study (a fixed debugThis2.py), let's split up the trial-generation part from the rest of the experimental script:
# 
# 1. Place the code and functions related to generating trials into a separate file `generateTrials.py`. 
# 1. Edit generateTrials.py code so that instead of returning `trials`, it writes the trial info to a CSV file called trials.csv which contains in each row all the information needed for the current trial, separated by commas. This first row of this file should contain a column header:
# >isMatch,emotionPrompt,shownActor,shownCategory,targetFaceImage
# 1. Inside the main script, import you trial-generation function like so:
# ```Python
# from generateTrials import *
# ``` 
# (your generateTrials.py file should be in the same directory as your main experiment .py file):
# 1. In your main experiment script, call `generateTrials()` This should have the effect of creating trials.csv. 
# 1. Now let's read trials.csv into a list of dictionaries using [this importTrials function](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Psychopy_reference.html#Importing-a-trial-list)
# 

# You should now have a trialList that you can access like so:
# ```Python
# trialList = importTrials('trialList.txt')
# for curTrial in trialList:
#     curTrial['isMatch'] #contains 1/0 depending on whether the current trial is a match or mismatch
# ```

# Why did we go through the trouble of writing to a reading from a file? To have an extra record of the trial list to which a particular subject was exposed and to double-check that the distributions of different conditions are what we want.

# ## Prompt for the subject code
# Let's add the capability to collect the subject's code. Pop up a box (as you did in [Exercise 2](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Exercise2-names.html) prompting the experimenter to provide a subject code. Pass this values to `generateTrials()` and have generateTrials use it to create not a generically named trials.csv, but a trials file specific to this participant, e.g., if the subject code is `ec_101`, the trials-file should be `ec_101_trials.csv`
# 
# <div class="alert alert-block alert-info">
# You'll need to modify your importTrials call so that you're including the subject name there as well instead of the generic trialList.txt. Also remember to add gui to the `from psychopy import...` statement at the start of the file</div>
# 

# ## Create an output file
# Now let's create an output file containing our data! Have your main script write to a subjCode_data.csv file. Each line should correspond to a trial and contain the following information, in this order:
# 
# Independent Variables:
# * Subject Code
# * isMatch (0/1)
# * emotionPrompt ('Happy','Angry', or 'Sad')
# * shownActor (must be one of actors.keys())
# * shownCategory ('Happy','Angry', or 'Sad')
# * targetFaceImage (the filename of the face being shown, e.g., 005wN_90_60.jpg)
# 
# Dependent Variables:
# * accuracy (1 for correct/0 for incorrect)
# * Reaction time (in milliseconds)

# # Exercise 5b: A more interesting face categorization study 

# Here's a more interesting version of the expressions categorization experiment. The code below will show a prompt (Happy, Angry, or Sad) as before, and then show you three faces (one of which displayes the prompted expression). The user should respond with the the 1 key the prompted expression is on the left, the 2 key if it's in the middle, and the 3 key if on the right. 
# 
# <div class="alert alert-block alert-info">
# Note that the key codes are strings '1', '2', '3' not integers 1, 2, 3
# </div>

# In[ ]:


import random
import random
import sys
import numpy as np
from psychopy import visual, core, event

categories = {'Happy':'F', 'Angry':'W', 'Sad':'T'}
actors = ['001m', '001w', '002m', '002w', '003m', '003w', '004m', '004w', '005m', '005w']
suffix = '_90_60.jpg'
positions = {'left':(-190,0), 'middle':(0,0), 'right':(190,0)}
responseMapping = {'left':'1','middle':'2','right':'3'}

def randomButNot(l,toExclude,num):
	chosen = random.sample(l,num)
	while toExclude in chosen:
		chosen = random.sample(l,num)
	return chosen

def generateTrials(numTrials):
	trials=[]
	for i in range(numTrials):
		targetCategory = random.choice(categories.keys())
		distractorCategories = randomButNot(categories.keys(),targetCategory,2)
		actorsToShow = np.random.choice(actors,3) 
            #this is the random.choice() function from the numpy library which samples 
            #with replacement. cf. random.sample() samples WITHOUT replacement
		targetLocation = random.choice(positions.keys())
		trials.append({
					'emotionPrompt':targetCategory,
					'targetImage':actorsToShow[0]+categories[targetCategory]+suffix,
					'distractorImage1': actorsToShow[1]+categories[distractorCategories[0]]+suffix,
					'distractorImage2': actorsToShow[2]+categories[distractorCategories[1]]+suffix,
					'targetLocation': targetLocation
					})
	return trials


trials = generateTrials(40)

win = visual.Window([1024,700],color="black", units='pix')
prompt = visual.TextStim(win=win,text='',color="white",height=60)
correctFeedback = visual.TextStim(win=win,text='CORRECT',color="green",height=60)
incorrectFeedback = visual.TextStim(win=win,text='ERROR',color="red",height=60)
pic1 = visual.ImageStim(win=win, mask=None,interpolate=True)
pic2 = visual.ImageStim(win=win, mask=None,interpolate=True)
pic3 = visual.ImageStim(win=win, mask=None,interpolate=True)

for curTrial in trials:
	win.flip()
	core.wait(.25)
	prompt.setText(curTrial['emotionPrompt'])
	prompt.draw()
	win.flip()
	core.wait(.5)

	win.flip()
	core.wait(.1)
	pic1.setImage('faces/'+curTrial['targetImage'])
	pic2.setImage('faces/'+curTrial['distractorImage1'])
	pic3.setImage('faces/'+curTrial['distractorImage2'])
	pic1.setPos(positions[curTrial['targetLocation']])
	distractorPositions = randomButNot(positions.keys(),curTrial['targetLocation'],2)
	pic2.setPos(positions[distractorPositions[0]])
	pic3.setPos(positions[distractorPositions[1]])

	pic1.draw()
	pic2.draw()
	pic3.draw()
	win.flip()
	response = event.waitKeys(keyList=responseMapping.values())[0]
	print response,responseMapping[curTrial['targetLocation']]
	if response==responseMapping[curTrial['targetLocation']]:
		correctFeedback.draw()
	else:
		incorrectFeedback.draw()
	core.wait(.5)


# ## Modularize the generateTrials code
# Begin by modularizing the generateTrials() code as in Exercise 5a.

# ## Effect of spatial grouping?
# Notice how we're displaying the faces in a horizontal orientation. This allows for having the mouths and eyes nicely aligned which may help comparing faces. Let's see if there's an effect of this by intermixing trials with the three faces horizontally oriented as in the code above, and trials that are vertically oriented. To get you started, you'll want to do is update your positions dictionary to this:
# 
# ```Python
# positions = {
# 			'vertical':  {'bottom':(0,-190), 'middle':(0,0), 'top':(0,190)},
# 			'horizontal': {'left':(-190,0), 'middle':(0,0), 'right':(190,0)}
# 			}
# ```
# 
# You'll then want to introduce a position factor `positionType` which is 'vertical' or 'horizontal' (`positions.keys()`) and based on whether a given trial is 'vertical' or 'horizontal' you'll want to:
# 
# 1. Access the appropriate positions for setting where your pictures appear. E.g., if your current position type is stored in `curPositionType`, use `positions[curPositionType]` to access the dictionary containing the possible positions.
# 2. Set the location of the matching face by using e.g., `random.choice(positions[curPositionType].keys())`

# ## Use a mouse for responding
# It becomes awkward to use a keyboard for responding in a task like this, so let's use a mouse for responding. See [here](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Psychopy_reference.html#How-do-I-have-people-respond-with-a-mouse?) for sample mouse code. You'll want to display the three faces until a person clicks on one of them.

# ## Create an output file
# Now let's create an output file containing our data! Have your main script write to a subjCode_data.csv file. Each line should correspond to a trial and contain the following information, precisely in this order:
# 
# Independent Variables:
# * subject code (the unique subject code for the subject being run)
# * position type ('vertical' or 'horizontal')
# * emotion prompt (the string 'Happy', 'Angry' or 'Sad')
# * targetActor (must be one of actors.keys())
# * distractor1Actor (must be one of actors.keys())
# * distractor2Actor (must be one of actors.keys())
# * distractorEmotion1 (the string 'Happy', 'Angry' or 'Sad')
# * distractorEmotion2 (the string 'Happy', 'Angry' or 'Sad')
# * targetImage (the filename corresponding to the correct response, e.g., '005wN_90_60.jpg')
# * distractorImage1 (the filename corresponding to the first distractor)
# * distractorImage2 (the filename corresponding to the second distractor)
# * targetLocation (the location of the target: bottom/middle/top/left/right)
# 
# Dependent Variables:
# * isRight (1 if response is correct; 0 if incorrect)
# * emotionChosen (the chosen emotion (Happy/Angry/Sad; should equal emotionPrompt if the response is correct)
# * RT (Reaction time in milliseconds from when faces appeared to mouseclick on one of them)

# You may run into some trouble figuring out the emotion of the face that the participant clicked on. 
# If you set your `generateTrials()` function correctly, the following code will work:
# 
# 
# ```Python
# isRight = int(pic1.contains(response))
# if isRight:
#     correctFeedback.draw()
#     emotionChosen = curTrial['emotionPrompt']
# else:
#     incorrectFeedback.draw()
#     if pic2.contains(response):
#         emotionChosen = curTrial['distractorEmotion1']
#     elif pic3.contains(response):
#         emotionChosen = curTrial['distractorEmotion2']
# ```
# 

# ## Run yourself on the task!
# Please run yourself on this task to produce 100 trials of data. Should take <10 mins. Please take care to have your output file be precisely in the above-mentioned format so that we can combine data from everyone in the class. Here is a [sample output file](http://sapir.psych.wisc.edu/classMaterials/psych711/sample_data.csv). To check that your data is in the correct format, do the following:
# 
# At the terminal, inside 
# `cat sample.csv your_data.csv > data_format_test.csv`
# 
# (replacing your_data.csv with the name of your output file, and including the appropriate path to sample_data.csv if it's not in the same directory as your data)
# 
# Load the data into R:
# 
# 
# In R: `dat <- read.csv('data_format_test.csv')`
# 
# Look at the summary: `summary(dat)`
# 
# 
# 

# ## Bonus: Actor + positionType
# Let's cross the actor and positionType to see if e.g., having faces lined up in horizontally helps especially when they're all of same gender. You want to have the following trial distribution
# 
# ```
# horizontal (50%). Of these:
# same-gender(Male) - 25%
# same-gender(Female) - 25%
# different-gender - 50%
# 
# vertical (50%). Of these:
# same-gender(Male) - 25%
# same-gender(Female) - 25%
# different-gender - 50%
# ```
# 
# 
# To cross factors, you can use for-loops, but a more compact way is to use the [`itertools` package](https://docs.python.org/2/library/itertools.html). So you might want to do something like this:

# In[7]:


from itertools import product

positions = {
			'vertical':  {'bottom':(-190,0), 'middle':(0,0), 'top':(190,0)},
			'horiontal': {'left':(0,-190), 'middle':(0,0), 'right':(0,190)}
			}

genderMix = {'same-gender':['male','female'], 'diff-gender':[]}


trialTypes = list(product(positions.keys(), genderMix.keys()))

print trialTypes


# In[ ]:




