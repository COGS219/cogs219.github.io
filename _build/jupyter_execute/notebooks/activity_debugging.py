#!/usr/bin/env python
# coding: utf-8

# # Debugging practice
# 
# Debugging your code is an inescapable part of coding just like revising your writing is an inescapable part of writing. These exercises are designd to help you practice your debugging skills while demonstrating a few common pitfalls.
# 

# 1. This bit of code is supposed to iterate through a shuffled list. Why is it not working?

# In[53]:


import random
vowels = random.shuffle(['a','e','i','o','u'])

for cur_vowel in vowels:
	print(cur_vowel)


# 2. `Sets` are like lists except they allow us to perform set operations like union, intersection, difference etc. Unlike lists which have no restrictions on duplicated elements, a set -- by definition -- only contains unique elements. Because sets are implemented in a very efficient way, we can use them to remove duplicates from a list. For example:

# In[6]:


list_with_duplicates = ['dog', 'cat', 'wolf', 'dog', 'dog']
print(list_with_duplicates)
print(list(set(list_with_duplicates))) #voila, duplicates gone!


# I'm trying to do something similar here, but running into a problem. Help!

# In[58]:


duplicated_list = (violin, 'guitar', 'guitar', '3',3)
print(list(set(duplicated_list))) #voila, duplicates gone?


# 1. I'm trying to iterate through a list, check if each element is a palindrome (reads the same backwards and forwards), and remove all the non-palindromes so that so that at the end I only have palindromes. The palindrome checker is working... but something else is not. Fix it! Also what is ths .replace(' ','') doing?

# In[37]:


def is_palindrome(str):
    str = str.replace(' ','') # remove spaces
    return str == str[::-1]

list_of_strings = ['dog', 'rotator', 'dod', 'cat', 'kayak', 'malyalam', 'a man a plan a canal panama']

for i,j in enumerate(list_of_strings):
    if not is_palindrome(j.replace(' ','')):
        list_of_strings.remove(i)
print(list_of_strings)


# 5. I'm trying to iterate through a list, but something is wrong. What happened?
# 

# In[12]:


myList = []
for i in range(10):
    myList.append(i)

listSize = len(myList)
for index in range(listSize+1):
    print(myList[index])


# 1. Now instead of a list, I'm trying to iterate through a dictionary and print out just the car *models* stored inside it. (Stelvio, M3, etc.) Why isn't it working?

# In[16]:


thisDict = {
    'brand':['Alfa Romeo','BMW','Chevrolet','Dodge'],
    'year':[2018,2023,1997,1969],
    'model':['Stelvio','M3','Corvette','Challenger'],
    'color':['black','green','red','black'],
    'horsepower':[280,473,345,425]
}

for key in thisDict):
    print(thisDict[key])


# 1. The function I defined is supposed to compute the factorial of the number (y!), but it's not working. 

# In[49]:


def compute_factorial(y):
    for i in range(y,-1):
        y*=i
    return y

print(compute_factorial(5)) #should return 120 (5*4*3*2*1)... 


# 1. I'm trying to create a function that multiplies the number I input by 3, but why do I get `None`?

# In[22]:


def multiply_by_three(x):
    x*=3

a = 5
x = multiply_by_three(a)
print(x)

