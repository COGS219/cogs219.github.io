#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#Exercise-9---Face-Morph" data-toc-modified-id="Exercise-9---Face-Morph-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Exercise 9 - Face Morph</a></span></li></ul></div>

# # Exercise 9 - Face Morph
# 
# This example shows you how to implement a task where you want subjects to smoothly adjust stimuli along some dimension. In this case that dimension spans two faces, e.g., a male and a female face, or an angry and a happy face. The same procedure can be used for other types of visual stimuli as well.

# <video controls src="images/emotion_adjust.mov" />
# 

# Like [Exercise 8](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Exercise8-orientation.html), we're going to use the mouse-wheel/trackpad for adjustments. This time though the adjustments will affect which image we are seeing. When done properly, the result is a smooth continuum as shown in the movie above.

# Our trial list (`trials/sampleTrials.csv`) will look like this:

# ```
# morphType,trialIndex,stimGender,iteration,continuum,continuumCode,direction,filename
# gender,0,NA,0,NA,NA,right,malefemalemorph_
# gender,1,NA,1,NA,NA,left,malefemalemorph_
# emotion,0,man,0,sad-ang,SA,left,manSA_
# emotion,2,woman,0,ang-hap,HA,left,womanHA_
# emotion,3,woman,0,ang-hap,HA,right,womanHA_
# emotion,4,man,1,sad-ang,SA,left,manSA_
# emotion,5,man,1,sad-ang,SA,right,manSA_
# emotion,6,woman,1,ang-hap,HA,right,womanHA_
# emotion,7,woman,1,ang-hap,HA,left,womanHA_
# ```

# The code below reads in these trials (notice that we're using a pandas dataframe to do it; we will cover pandas in a few weeks, but feel free to [http://pandas.pydata.org/pandas-docs/stable/10min.html](read up on it) in the meantime).
# 
# We then go through the trials one by one, and draw the picture contains in the filename column + a three-digit number (001 to 120) which is the frame-number, with 60 being the midpoint.

# In[ ]:


import os
import random
from psychopy import visual, core, event
import pandas as pd
from useful_functions import loadFiles


win = visual.Window([800,700],color="gray", allowGUI=False, units='pix')
myMouse = event.Mouse(win=win,visible=False)

visual.TextStim(win,text="Loading images...", color="black",height=40).draw()
win.flip()



def showText(win,text,color,mouse):
```
Displays text and waits for a mouse press or keyboard press
This would ordinarily go into your useful_functions library```
```
    visual.TextStim(win,text=text,color=color,height=30).draw()
	win.flip()
	if mouse:
		while True:
			while any(mouse.getPressed()):
				if not any(mouse.getPressed()):
					return
	else:
		event.waitKeys()
		return

pics = loadFiles('stimuli','jpg','image',win)
emotionMorphText="Adjust the emotion of the face by moving the mouse wheel up or down until you find the point at which one emotion transitions to another emotion. When you are satisfied, click the left mouse button to go on to the next picture."
genderMorphText="Adjust the gender of the face by moving the mouse wheel up or down until you find the transition from male-to-female or female-to-make. When you are satisfied, click the left mouse button to go on to the next picture."

delta = 1
maxStimNum=120
expTimer = core.Clock()

trials = pd.read_csv('trials/sampleTrials.csv')
trials = trials.to_dict('records')


def runTrial(curTrial):
		if curTrial['direction']=='left':
			stimNum='1'.zfill(3)
		else:
			stimNum=str(maxStimNum)
		win.flip()
		core.wait(1.0)
		win.flip()
		respTimer = core.Clock()
		numWheelTurnsUp = numWheelTurnsDown = 0
		
		while True:
			wheelRel = myMouse.getWheelRel()[1]
			if wheelRel<0.0:
				numWheelTurnsDown+=1
				if int(stimNum)>1:
					stimNum = str(int(stimNum)-delta).zfill(3) 
			elif wheelRel>0.0:
				numWheelTurnsUp+=1
				if int(stimNum)<maxStimNum:
					stimNum = str(int(stimNum)+delta).zfill(3) 
			elif myMouse.getPressed()[0]==1:
				rt = respTimer.getTime()
				if rt>.8 and (numWheelTurnsUp>0 or numWheelTurnsDown>0):
					break
			pics[curTrial['filename']+str(stimNum)]['stim'].draw()
			win.flip()

for curTrial in trials:
	print curTrial['trialIndex'], curTrial['morphType']
	if curTrial['trialIndex']==0 and curTrial['morphType']=="emotion":
		showText(win,emotionMorphText,color="black",mouse=myMouse)
	elif curTrial['trialIndex']==0 and curTrial['morphType']=="gender":
		showText(win,genderMorphText,color="black",mouse=myMouse)

	runTrial(curTrial)

