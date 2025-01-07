#!/usr/bin/env python
# coding: utf-8

# # Debugging practice
# 
# It's easier to work with .py versions of these files. They are located in [here](https://github.com/psych750/activity_debugging_experiments) along with the necessary image/sound files to run this code.
# 
# ## Practice 1
# Here's some broken code. When fixed, it should display wide and narrow
# rectangles, in random order, and play a bleep sound if you respond 'w'
# for wide or 'n' for narrow, and buzzing sound otherwise. It should
# also output the correctness of the response and the RT to the console/terminal (a.k.a. `standard
# output`. The .wav files it uses are available [here](https://github.com/psych750/activity_debugging_experiments) - the same repository you cloned for the previos activity.

# In[ ]:


import time
import random
from psychopy import visual, core, event,sound
win = visual.Window([800,600],color="blak", units='pix')

rect = visual.Rect(win,fillColor="blue",size=size)
aspect = {'wide':[200,100], 'narrow':[100,200]}
validKeys = {'wide':'w', 'narrow':'n'}

bleep = sound.Sound('sounds/bleep.wav')
buzz = sound.Sound('sounds/buzz.wav')

for curIter in range(20)
	win.flip()
	core.wait(.5)
	curAspect  = random.choice(aspect.values())
	rect.setSize(aspect[curAspect])
	rect.draw()
	win.flip()
	timer = core.Timer()
	resp = event.waitKeys(keyList=validKeys.values())
	if resp==validKeys[aspect]:
		print 1, timer.getTime()
		bleep.play()
	else:
		print 0, timer.getTime()
		buzz.play()


# ## Practice 2
# Here's some more broken code. This program should prompt you with an expression category (Happy, Sad, etc.) and then show a face. If you categorize the face correctly (or at least normatively), you should see a green CORRECT. Otherwise a red ERROR. The program should present you with 40 trials. The faces are avaialble in [this repository](https://github.com/psych750/activity_debugging_experiments) (that you should've already cloned for the previous activity)

# In[1]:


from psychopy import visual, core, event

categories = {'Happy'='F', 'Angry'='W', 'Sad'='T'}
actors = ['001m', '001w', '002m', '002w', '003m', '003w', '004m', '004w', '005m', '005w']
suffix = '_90_60.jpg'
responseMapping = {'up':1,'down':0}
numTrials = 40


def randomButNot(l,toExclude):
	chosen = random.choice(l)
	while toExclude in chosen:
		chosen = random.choice(l)
	return chosen

def generateTrials(numTrials):
	trials=[]
	propMatch  = .6
	for i in range(numTrials):
		emotionPrompt = random.choice(categories.keys())
		shownActor = random.choice(actors)
		isMatch = int(random.random()<propMatch)

		if isMatch:
			shownCategory = emotionPrompt
			targetFaceImage = shownActor+categories[emotionPrompt]+suffix
		else:
			shownCategory = randomButNot(categories.keys(), emotionPrompt)
			targetFaceImage = shownActor+categories[shownCategory]+suffix

		trials.append({	'isMatch':isMatch,
						'emotionPrompt':emotionPrompt,
						'shownActor':shownActor,
						'shownCategory':shownCategory,
						'targetFaceImage':targetFaceImage
						})

		return trials

trials = generateTrials(numTrials)

win = visual.Window([800,600],color="black", units='pix')
prompt = visual.TextStim(win=win,text='',color="white",height=60)
correctFeedback = visual.TextStim(win=win,text='CORRECT',color="green",height=60)
incorrectFeedback = visual.TextStim(win=win,text='ERROR',color="red",height=60)
pic = visual.ImageStim(win=win, mask=None,interpolate=True)

for curTrial in trials:
	win.flip()
	core.wait(25)
	prompt.setText(curTrial['emotionPrompt']+'?')
	prompt.draw()
	win.flip()
	core.wait(.5)

	win.flip()
	core.wait(.1)
	pic.setImage('faces/'+curTrial['targetFaceImage'])
	pic.draw()
	win.flip()
	response = event.waitKeys(keyList=responseMapping.values())[0]
	if response==responseMapping[curTrial['isMatch']]:
		correctFeedback.draw()
	else:
		correctFeedback.draw()
	win.flip()
	core.wait(.5)

