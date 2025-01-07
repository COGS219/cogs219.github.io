#!/usr/bin/env python
# coding: utf-8

# # Playing around with dictionaries

# ## Practice with operations on dictionary values
# 
# Here's a [deep thought (by Jack Handey)](https://philip.greenspun.com/humor/deep-thoughts)

# In[6]:


a_deep_thought = '''Probably the earliest flyswatters were nothing more than \ 
some sort of striking surface attached to the end of a long stick'''


# Let's create a dictionary out of it where each word is a key and its number of characters is a value.

# In[5]:


deep_thought_dict = {}
for cur_word in a_deep_thought.split(' '):
    deep_thought_dict[cur_word.lower()]=len(cur_word)
print(deep_thought_dict)


# :::{tip}
# Common operations like this often have one-line solutions. We can accomplish the same behavior without an explicit `for` loop by using [dictionary comprehension](https://www.programiz.com/python-programming/dictionary-comprehension):
# ```python
# deep_thought_dict = {cur_word.lower(): len(cur_word) for cur_word in a_deep_thought.split(' ')}
# ```  
# :::

# Now that we have this information in a dictionary, do the following:
# 
# * What's the average number of characters in these words?
# 
# :::{tip} 
# To find an average use `mean()` from the `numpy` library. For example,
# ```python
# import numpy as np
# print(np.mean(range(10)))
# ```
# You may need to explicitly convert the argument to np.mean to a list by using `list()`
# :::
# 
# 
# * What's the average number of characters in words beginning with vowels? 
# 
# :::{tip}
# By taking advantage of statements that already return True/False values, the code below avoids having to have code like: if X return True, else return Y. You don't necessarily want to use this exact code; it's just a demonstration.
# ```python
# def is_vowel(letter):
#     return letter in ['a','e','i','o','u']
# ```
# :::
# 
# ```{dropdown} Challenge
# Can you do this in one line of code? (hint: you'll need to use list comprehension)
# ```
# 
# 
# 

# * Now return the mean length of words beginning with a consonant
# ```{tip}
# You don't need to write a separate function for consonants!
# ```
# 

# ## Using a dictionary as a look-up table
# 
# Dictionaries are a useful data-type for dynamically choosing actions based on the value of some variable.
# 
# For example, suppose we want to show different stimuli based on whether participant responded with a particular arrow key (up, down, left, right). Depending on their response, we want to update the position of a stimulus, moving it 10 pixels to the right, left, etc.We might initially write code like this:
# 
# ```python
# if resp == 'left':
#     stim.pos += (-10,0)
# elif resp == 'right':
#     stim.pos += (10,0)
# elif resp == 'up':
#     stim.pos += (0,10)
# elif resp == 'down':
#     stim.pos += (0,-10)
# ```
# 
# This is bearable if we have just 4 alternatives, but what if we have 10? 30? Remember, anytime you're finding yourself repeating a piece of code with minor variation, there's gonna be a better way. In this case, one better way is to use dictionaries.
# 
# ```python
# resps_to_positions = {'left':(-10,0), 'right':(10,0)}
# ```
# 
# Finish this activity by specifying the rest of the dictionary. Then rewrite the conditional above to use this dictionary, replacing the multi-pronged conditional with a single line of code. That is, if you have a response stored in `resp`, how do you return the corresponding position?
# 

# ## Create and iterate through a list of dictionaries
# 
# Another common use of dictionaries is to allow for structured access to information (this is quite relevant for Exercise 4). In Exercise 3, the trial file you generated had a bunch of columns that you had to access with their indices requiring you to keep track of which column number contained what information (color, orientation, etc.). Let's try to use a dictionary to do this instead.
# 
# Below is some code to generate pairs or pets and owners. Right now it just prints the pairs. Modify the code so that the pairs are instead stored in a `pet_owners` list where each element contains two keys 'pet' and 'owner' and the value of the keys are the specific pet and specific owner, respectively. Then iterate through the list and print out the values.

# In[7]:


import random
pets = ['dog','cat','goldfish','hamster']
owners = ['caleb','zihan','kelly','tianrun']

num_rows = 10

for rows in range(num_rows):
    print(random.choice(pets),random.choice(owners))


# ## 
