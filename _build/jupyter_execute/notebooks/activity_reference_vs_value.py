#!/usr/bin/env python
# coding: utf-8

# # Mutables, Immutables, and Object References
# 
# This section introduces a couple distinctions: **mutable** vs. **immutable**, and **passing by value**, by **reference**, and by **object reference**. You can read about this in more detail [here](https://secon.utulsa.edu/cs2123/slides/pypass.pdf) and [here](https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/#:~:text=Python%20utilizes%20a%20system%2C%20which,being%20passed%20to%20the%20function.). Another good source with some helpful illustrations is [this explanation](https://blog.finxter.com/how-to-pass-a-variable-by-reference-in-python/).
# 
# If you want a bit more of a brain melt, check [this out](https://medium.datadriveninvestor.com/mutable-and-immutable-python-2093deeac8d9).
# 
# 
# Python's variable types come in two main flavors: immutables and mutables. 
# 
# **Immutables**
# 
# An immutble is a variable whose internal state cannot be changed. Numbers (integers and floats), strings, booleans, and tuples are all of this kind. The internal value of 5 is... 5. An 's' is an 's'. A True is a True. 
# 
# **Mutables**
# 
# A mutable type is the opposite -- a variable whose internal value *can* be changed. Lists, dictionaries, and more complex user-defined objects (for example the various psychopy objects we've been working with like `win`, `visual.Rect`, etc.
# 
# 
# When we pass variables between functions or between a function and the main code block, the information the variables contains is passed differently depending on whether the variable is mutable or immutable. Immutable variables are passed by value while mutable variables are passed by reference (i.e., what's passed is the pointer to the memory location of that object, not the object's contents).
# 
# Understanding this distinction will improve your mental model of how information is passed around in a python program and helps to understand why some things may not work the way you initally expect them to.   

# Predict what happens in these next two cells

# In[1]:




a_fruit = 'apple'
another_fruit = 'mango'

another_fruit = a_fruit 
a_fruit *= 2

print(a_fruit)
print(another_fruit)


# In[2]:




fruits = ['apple', 'pear']
more_fruits = ['mango', 'watermelon']

more_fruits = fruits 
fruits.append('avocado')

print(fruits)
print(more_fruits)


# Weird, right? In the first cell, we're dealing with variables containing strings (an immutable type). When we did `another_fruit = a_fruit `, the value of `a_fruit` was assigne to the variable `another_fruit` (if it already had a value, it was overwritten). In other words, the information was passed by **value**. The two variables -- `fruit` and `another_fruit` are completely independent from one another.
# 
# 
# In the second cell we are dealing with a **mutable** type -- a list. When we assigned one list to another variable -- `more_fruits = fruits` -- the **reference** of the list (its location in memory) was passe to the variable `more_fruits`. What happens now is that both variables -- `fruits` and `more fruits` are pointing to the same place in memory. In effect they are the same object. And so changing one will change the other (because what we are changing is a list that both varibles are pointing to). 
# 
# 
# The distinction is especially important to understand because it underpins how information is passed between functions/namespaces.  Let's take a look at these couple examples. Predict the output of each cell.

# In[3]:


def change(x):
    x = x+5
    return x

a_num = 4
a_num = change(a_num)
print(a_num)


# In[4]:


def change(x):
    x = x+5

a_num = 4
change(a_num)
print(a_num)


# In[5]:


def change(x):
    x.append(5)

a_list = [4]
change(a_list)
print(a_list)


# In[1]:


def change(x):
    x.append(6)

a_list = [4]
change(a_list)
print(a_list)


# In[7]:


def change(x):
    x.append(5)
    return x

a_list = [4]
b_list = change(a_list)
print(b_list)
print(a_list)

