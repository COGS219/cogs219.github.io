#!/usr/bin/env python
# coding: utf-8

# # List comprehension
# 
# ## The idea
# List comprehension provides a compact way to take a list, do something to the elements (modify, filter, apply a function), and then return the resulting list. See some examples [here](http://www.pythonforbeginners.com/basics/list-comprehensions-in-python).

# ## The syntax
# 
# List comprehension expressions are embedded in [] as a way to signal that the result is a list. For example:

# In[3]:


[num**2 for num in range(10)]


# Reading the above statement from right to left, here's what's happening:
# 
# `range(10)` - generate a list
# 
# `...for num in...` iterate through it using `num` as the iterator variable
# 
# `num**2` the thing that you're doing to the list. Here, squaring each element.
# 

# By including `if` statements inside list comprehension, you can effectively filter a list for the elements you want (or don't want)

# In[12]:


[num**2 for num in range(10) if num %2 ==0]


# You can also embed multiple lists inside a list-comprehension expression. This is equivalent to nested loops, but I personally find these confusing.

# In[13]:


[first+second for first in ['a','b','c'] for second in ['d','e','f']]


# ### Dictionary Comprehension

# In addition to *list* comprehension, Python also implements *dictionary* comprehension. I include an example for completeness, though I find myself using this quite rarely. The example below checks if a phrase is a pangram, 

# In[23]:


sentence = "Just a simple little sentence the word lengths of which we can count in one line"
wordLengths = {key: len(key) for key in sentence.split(' ')}


# ## Exercises

# ### Find all of the numbers from 1-1000 that are divisible by 9

# In[10]:


[num for num in range(1,1001) if num % 9 ==0]


# ### Generate 100 random numbers in the range 0-1 using one line of code

# In[12]:


import random
[random.random() for num in range(100)]


# ### Generate 100 random integers in the range 1-10 using one line of code

# In[26]:


import random
[random.randrange(1,11) for num in range(100)]


# ### Return a list of words longer than 3 letters.
# Use list comprehension to take `sentence` and output the words containing more than 3 letters

# In[29]:


sentence = 'The Quick Brown Fox Jumped Over The Lazy Dog'
[word for word in sentence.split() if len(word)>3]


# ### A list of all consonants
# Return a list containing all the consonants in `sentence`. The consonants don't have to be unique, but the list should not have both uppercas and lowercase letters. You should do this in one line of code.
# ```{note}
# Use str.isalpha() to check for punctuation. E.g., 'word'.isalpha() returns True while '?'.isalpha() and 'a word'.isalpha() return False 
# ```

# In[34]:


sentence = 'Can you figure out how many CONSONANTS are in this sentence?'
vowels = ['a','e','i','o','u'] 

[letter for letter in sentence.lower() if (letter not in vowels and letter.isalpha())]
#insert your code here


# Use *dictionary* comprehension to count the length of each word in a sentence. 

# In[35]:



sentence = 'Use a dictionary comprehension to count the length of each word in a sentence' 
results = {word:len(word) for word in sentence.split()} 
print(results) 


# ### Dictionary refresher
# ```{admonition} Challenge
# Add a line to the code below to get the average word length in `sentence`
# Hint: `sum(a_list)` returns the sum of the elements in the list
# ```

# In[3]:


sentence = "Just a simple little sentence, the word lengths of which we can count in one line"
wordLengths = {key: len(key) for key in sentence.split(' ')}
sum(wordLengths.values())/len(wordLengths.values())


# In[ ]:




