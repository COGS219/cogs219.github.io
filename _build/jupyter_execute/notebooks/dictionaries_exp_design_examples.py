#!/usr/bin/env python
# coding: utf-8

# Using dictionaries in experiment design: some examples
# ===
# 
# What are some real-world examples of using dictionaries in your experiment?
# 
# Recall part 7-8 of [Exercise 2](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Exercise2-names.html). The information entered into the pop-up boxes is stored in... a dictionary! When you execute the statements 
# 
# ```Python
# userVar = {'Name':'Enter your name'}
# dlg = gui.DlgFromDict(userVar)
# ```
# 
# You are creating a dictionary named `userVar` and then setting the Name key in the dictionary with the value the user enters into the box. The userVar can have multiple keys, e.g.
# 
# ```Python
# userVar = {'Name':'Enter your name', 'Age':'Enter your age'}
# dlg = gui.DlgFromDict(userVar)
# ```
# 
# See [here](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Psychopy_reference.html#Easy-way-to-get-runtime-variables) for how to extend this general approach to a more real-world situation.
# 

# Here is another example in which we check whether the received response is equal to the correctResponse. Assume that correct_response is set to 'match' or 'mismatch'

# In[ ]:


response_mapping = {'z':'match', 'slash':'mismatch'}

if response_mapping[response_received] == correct_response:
    isRight=1
else:
    isRight=0


# Suppose we want to have a counterbalancing variable such that people assigned to the *matchLeft* condition response with 'z' as match and 'slash' as mismatch while people assigned to the *matchRight* condition have the response keys reversed. We could do if/else statements, but dictionaries provide a more elegant and more extendible solution:

# In[ ]:


response_mapping = {
                    'matchLeft': {'z':'match', 'slash':'mismatch'},
                    'matchRight': {'z':'mismatch', 'slash':'match'}}

whichMatch = 'matchLeft' #this would be ordinarily set at experiment runtime
response_received = event.waitKeys(keyList = response_mapping[whichMatch].keys())

if response_mapping[whichMatch][response_received] == correct_response:
    isRight=1
else:
    isRight=0

