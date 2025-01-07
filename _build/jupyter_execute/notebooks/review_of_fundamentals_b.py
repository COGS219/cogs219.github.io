#!/usr/bin/env python
# coding: utf-8

# # Review of fundamentals B
# In this notebook, you will review the additional python syntax we've covered since the first review of fundamentals. You should be able to correctly predict what happens in all of these cases. If you get something wrong, figure out why!

# ## Lists, list comprehension, and randomization

# In[2]:


my_list = ['spam']
print(len(my_list))
print(len(my_list[0]))


# In[4]:


print(list(range(10)[-5:]))


# In[5]:


import random
my_list = ['a','b','c']*3 + ['c','d','e']*3
random.shuffle(my_list)
my_list[0:5]


# In[2]:


import random
my_list = ['a','b','c'] + ['c','d','e']
random.sample(my_list,7)


# In[7]:


import random
[round(random.random(),1) for i in range(15)]


# In[9]:


vowels = ['a', 'e', 'i','o','u']
print ([element*i for i,element in enumerate(vowels)])


# In[10]:


print (' '.join([' '.join((i, 'and a')) for i in ('one', 'two', 'three', 'four')]))


# In[11]:


responses = 'ccctcctttttcc'
[i for i,curResp in enumerate(responses) if curResp=='c']


# In[12]:


import random

positions = ['left', 'middle', 'right']
positions2 = positions

positions.append('bottom')
random.shuffle(positions2)

print (positions, positions2)
print (len(positions), len(positions2))
print (positions==positions2)


# ## Dictionaries

# In[22]:


positions = {'left':(-100,0), 'middle':(0,0), 'right':(100,0)}
[random.choice(list(positions.keys())) for i in range(10)]


# ```{note}
# In Python 2, dict.keys() returned a list. In Python 3 it returns a 'view' object which is fine if you want to see what the keys are, but won't work for subsetting or doing things like getting choosing a random element as we do here. To make it work, we must force it to be a list with `list()`
# ```

# ```{note}
# 

# In[23]:


positions = {'left':(-100,0), 'middle':(0,0), 'right':(100,0)}
[positions[random.choice(list(positions.keys()))] for i in range(10)]


# In[24]:


responses = 'ccctcctttttcc'
responsesMapping = {'c':'chair','t':'table'}
[responsesMapping[curResp] for curResp in responses]

