#!/usr/bin/env python
# coding: utf-8

# # Python basics

# ## Getting help
# 
# There are many places to turn to for a Python reference and basic
# help. The quickest way to get help on a function is to google
# `python what you're looking for`. Typically, Google will refer you
# to <http://docs.python.org/>. For example, try googling
# `python randomize`. Google is good. Below are some additional
# references:
# 
# [StackOverflow](https://stackoverflow.com)
# :    For example, try searching for "python randomize" on StackOverflow: <https://stackoverflow.com/search?q=python+randomize>
# 
# [Software Carpentry](https://software-carpentry.org/)
# :    Software Carpentry also has lectures and tutorials on Linux, Scientific Computing, and many other topics: <https://software-carpentry.org/lessons/>
# 
# [Python Visualizer](http://pythontutor.com/visualize.html)
# :    The Python Visualizer may be helpful if you are having trouble conceptualizing how python exectures some bit of code.
# 
# [NumPy for Matlab users](http://mathesaurus.sourceforge.net/matlab-numpy.html)
# :    If you're a Matlab user transitioning to Python, this page may be helpful.

# ## Quick references
# 
# -   Lists and list comprehension:
#     <http://docs.python.org/tutorial/datastructures.html#more-on-lists>
# -   Useful functions for Python dictionaries:
#     <https://docs.python.org/3.7/library/stdtypes.html>
# -   Writing/reading files:
#     <http://docs.python.org/tutorial/inputoutput.html#reading-and-writing-files>
# -   Sorting lists and dictionaries - nice tips for how to sort by a
#     particular key: <http://wiki.python.org/moin/HowTo/Sorting>
# 

# 
# ## Python mini tutorials and tips
# 
# ### Get help on a module
# 
# To get help on the functions contained in some module, for instance,
# the module 'string', type: `help('string')`

# In[1]:


help('string')


# Oo, look at that, learn something every time:

# In[2]:


import string
string.ascii_letters


# ### Notes on importing libraries and functions
# 
# Python provides a somewhat confusing variety of ways of importing functions and libraries.
# 
# ```python
# import X
# import X as Y
# from X import *
# from X import a,b,c
# X = __import__('X')
# ```
# 
# The differences and pros and cons are discussed in this excellent article: <http://effbot.org/zone/import-confusion.htm>

# ### To find out the version of the library you've imported:

# In[1]:


import nltk
nltk.__version__


# ### To find out the location of the source files that are being loaded when you import a library:

# In[2]:


import nltk
nltk.__file__


# ### Finding something in lists and strings
# 
# Supposed you have a list called shoppingList:

# In[4]:


shoppingList =  ['apples', 'oranges', 'screwdriver']


# And you want to determine if this list contains some item, say,
# 'apples'. The easiest way to do it is to use `in`.

# In[5]:


if 'apples' in shoppingList:
    print('yep')


# Now, suppose your shopping list is in a string called shopping list and
# you want to to determine if a string variable called shoppingList
# contains the word 'apples' in it.

# In[2]:


shoppingString =  'apples, oranges, screwdriver'


# Turns out `in` works here as well:

# In[7]:


if 'apples' in shoppingString:
    print('yep')


# The reason `in` operator works here is that `in` is defined for all
# sequences (lists, tuples, strings, etc.). Note, however, that in this
# case, there is an ambiguity. In the case of a shoppingList list,
# 'apples' is a standalone element. In the case of a shoppingList
# string, python doesn't know where one element starts and the next
# stops. Therefore, both of these statements will be true for
# shoppingStrings.

# In[3]:


'apple' in shoppingString


# In[10]:


'apples' in shoppingString


# ```{tip}
# If you want to search a string more flexibly, you can use [String.find](https://www.geeksforgeeks.org/python-string-find/) and regular expressions which we'll cover later in the term.
# ```

# but not for shoppingList

# In[11]:


'apple' in shoppingList


# In[12]:


'apples' in shoppingList


# Just as you can use `in` to check if an element is contained in a
# sequence, you can use `not in` to check if it's not in the sequence.

# ### Use Exceptions
# 
# See the Python doc on exceptions here
# <http://docs.python.org/tutorial/errors.html> The 'pythonic' way of
# doing things is to try it and catch the exception rather than check
# first.
# 
# For example, rather than doing this:
# 
# ```python
# if os.path.exists('name.txt'):
#     f = open('name.txt', 'r')
# else:
#     print('file does not exist')
#     sys.exit()
# ```
# 
# do this:
# 
# ```python
# try:
#     f = open('name.txt', 'r')
# except IOError:
#     print('file not found!')
#     sys.exit()
# ```
# 
# There are many cases where you **have** to use exceptions to keep your
# program from crashing, for example, division by 0.

# ### Using list comprehension
# 
# This
# 
# ```python
# print([letter for letter in 'abracadabra'])
# ```
# 
# is better than this
# 
# ```python
# for letter in 'abcracadabra'
#   print(letter)
# ```
# 
# Here's another example. Say you have a list of names and you want to split them into first and last names

# In[13]:


names = ['Ed Sullivan', 'Salvador Dali']
firstNames = [name.split(' ')[0] for name in names]
lastNames =  [name.split(' ')[1] for name in names]


# Another example: generate 10 random numbers in the range 1-5:

# In[4]:


import random

[random.randint(1,5) for i in range(10)]


# Or generate 10 random letters:

# In[6]:


import string
[random.choice(list(string.ascii_lowercase)) for i in range(10)]


# And yet another example, this one restricting the output using a
# conditional. Generate numbers from 0-7, but omitting 2 and 5:

# In[16]:


[location for location in range(8) if location not in [2,5]]


# [List
# comprehension!](http://docs.python.org/tutorial/datastructures.html#list-comprehensions)
# all the cool kids do it.
# 
# On the other hand.... think twice before obfuscating your code:
# 
# For example, the repetition function from Exercise 4 (trial generation) can be rewritten as a one-liner:

# In[9]:


def repetition(letters,numberBeforeSwitch,numRepetitions):
       print('\n'.join([item for sublist in  [[i] * numberBeforeSwitch for i in letters] for item in sublist] * numRepetitions))


repetition(['a','b','c'], 2, 2)


# It is fast and compact, but certainly not very clear.

# ### How to flatten a list
# 
# Say you've got a list like this:

# In[18]:


list1 = [['A','B'],['A','B'],['C','D'],['C','D']]


# But what you want is this:

# In[19]:


list2 = ['A','B','A','B','C','D','C','D']


# You can turn list1 into list2 (i.e., *flatten* list1), like so:

# In[20]:


list2 = [item for sublist in list1 for item in sublist]
list2


# The above method will only work for flattening lists of depth-1, see
# [here](http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html)
# for more information.
# 
# An alternative way of flattening a list is to use NumPy.

# In[21]:


import numpy
list1 = numpy.array(list1) # convert it to a numpy array
list1 = list1.flatten()    # flatten it
list1 = list(list1)        # convert it back to a Python list, if you want.
list1


# We can, of course, do it all in one line:

# In[22]:


list1 = list(numpy.array(list1).flatten())
list1


# (In cases like this, you can continue to work with the NumPy Array,
# which lets you do all sorts of [neat
# things](http://mathesaurus.sourceforge.net/matlab-numpy.html)).

# ### Detect sequences
# 
# Say you have a list and you want to know whether it has sequential elements (e.g., 3,4). Why would you care? Suppose you want to intersperse catch trials throughout your experiment, but you don't want to have two catch trials in a row. How to ensure this?

# In[12]:


import random

def has_sequential(lst):
	lst = sorted(lst)
	for elt in zip(lst,lst[1:]):
		if elt[1]-elt[0]==1:
			return True
	return False

repeatTrials = random.sample(range(180),20)
while has_sequential(repeatTrials):
    repeatTrials = random.sample(range(180),20)
print(sorted(repeatTrials))


# ### Shuffle a list slice in place
# To shuffle a list in place, we can use `random.shuffle(lst)`. But what if you want to shuffle only a part of the list? `random.shuffle(lst)` will shuffle the whole list (and unhelpfully return `None`). 
# 
# One option is to use a modified [Knuth (a.k.a. Fisher-Yates) shuffle](https://eli.thegreenplace.net/2010/05/28/the-intuition-behind-fisher-yates-shuffling/).

# In[4]:


import random
def shuffle_slice(a, start, stop):
    index1 = start
    while (index1 < stop-1):
        index2 = random.randrange(index1, stop)
        a[index1], a[index2] = a[index2], a[index1]
        index1 += 1

a = range(10)
print(a)
shuffle_slice(a,0,4)
print(a)


# ### Use sets
# 
# Don't reinvent the wheel. Operations like computing intersections,
# unions, and uniqueness are all well-defined functions in set
# notation and are built in to Python. See
# [here](http://docs.python.org/library/sets.html#set-objects). Some
# examples of sets:
# 
# Get the intersection (the elements in common)

# In[23]:


set('abc').intersection('cde')


# Get the union (all the elements)

# In[24]:


set('abc').union('cdef')


# Note that because, by definition, a set can only contain unique
# elements, they are a good way to get all the distinct elements in a
# list.

# In[25]:


spam = ['s','s','s','p','p','a','m']
set(spam)


# Caveat: sets are, by definition, not ordered, hence we are not
# guaranteed to get 's','p','a','m'.
# 
# Let's see what spam and ham have in common.

# In[26]:


set('spam').intersection('ham')


# And what they don't

# In[27]:


set('spam').difference('ham')


# ### Arithmetic and floating point notation
# 
# Python uses dynamic typing. This means that it attempts to
# automatically detect the type of variable you are creating.
# 
# For example

# In[28]:


spam = "can be fried"


# Assigns the string `can be fried` to the variable spam. It knows it's a
# string because it's in quotations

# In[29]:


spam = 3


# assigns spam to the integer 3, which is not the same as

# In[30]:


spam2 = '3'


# In[31]:


spam == spam2


# ```{tip}
# If you're not sure what type something is, use the `type()` function to check.
# ```

# ### Reference, mutability, and copying
# 
# Have a look at this:

# In[8]:


egg = 'green'
ham = egg
ham


# In[9]:


egg = 'yellow'
ham


# Easy enough. Now have a look here:

# In[10]:


egg = ['green']
ham = egg
ham


# In[11]:


egg[0] = 'yellow'
ham


# What do you think is happening here? That's right, ham points to the
# egg list, not to the content inside. When you change the content of the `egg` list, you've changed the value of the `ham` variable.

# ### Writing to a file, safely

# ```python
# import os
# fileHandle = open('dataFile.txt','w')
# fileHandle.write(line) # the line you are writing.
# fileHandle.flush()     # mostly unnecessary 
# os.fsync(fileHandle)   # ditto; it helps if you have several processes writing to the file
# ```

# At the end of your experiment:

# ```python
# fileHandle.close()
# ```

# ### Copy a file
# 
# To copy a file use shutil.copyfile(src, dst). src is the path and name
# of the original file. dst is the path and name where src will be copied.

# ```python
# import shutil 
# shutil.copyfile(src,dst)
# ```

# Examples

# ```python
# shutil.copyfile('1.dat', '3.dat')
# ```

# This copies 1.dat into a new file named 3.dat.

# ```python
# shutil.copyfile('1.dat', 'directory\\3.dat')
# ```

# This copies 1.dat into the specified directory as 3.dat. Notice the
# escape character before the slash.

# ### Create a new directory

# ```python
# import os
# os.makedirs(newDirectoryName)
# ```

# ### Some simple generator functions
# 
# Here's a function that implements an infinite list of odd numbers.

# In[16]:


def oddNum(start):
    while True:
        if start % 2 ==0:
            start+=1
        yield start
        start+=1


# Here's one way to use it:\
# Get 30 odd numbers starting at 1

# In[21]:


someOddNums = oddNum(1) #start it at 1
print(someOddNums)
for i in range(30):
    print(next(someOddNums))


# Here's another way using list comprehension:

# In[23]:


moreOddNums = oddNum(1) #start it at 1
[next(moreOddNums) for i in range(30)]


# Here's a generator function for implementing a circular list. If you
# pass in a number, it will create a list of integers of that length,
# i.e., `circularList(5)` will create a circular list from `[0,1,2,3,4]`. If
# you pass in a list, it will make a circular list out of what you pass
# in, e.g., `circularList(['a','b','c'])` will create a circular
# list from `['a','b','c']`)

# In[26]:


def circularList(lst):
    if not isinstance(lst,list) and isinstance(lst,int):
        lst = range(lst)
    i = 0
    while True:
        yield lst[i]
        i = (i + 1)%len(lst) #try this out to understand the logic


# To use it, create a new generator by assigning it to a variable:

# ```python
# myGenerator = circularList(lst)
# ```

# where `lst` is the list you'd like to iterate through continuously.
# Notice the conditional in the first line of the circularList function.
# This allows the function to take in either a list or an integer. In the
# latter case, the function constructs a new list of that length, e.g.,
# circularList(3) will iterate through the list [0,1,2] ad infinitum:

# In[30]:


myGenerator = circularList([0,1,2])
next(myGenerator)


# In[31]:


next(myGenerator)


# In[32]:


next(myGenerator)


# In[33]:


next(myGenerator)


# See what happens if you make a generator using a character string, e.g.,
# `myGenerator = circularList('spam').`

# Here's a slightly more complex version of the circularList generator.
# The basic version above iterates through the list always in the same
# order. It is more likely that you\'ll want to iterate through it in a
# less ordered way. The variant below shuffles the list after each
# complete passthrough. Moreover, the shuffling is controlled by a seed so
# that each time you run it with the same seed, you\'ll get the same
# sequence of randomizations.

# In[34]:


import random

def randomizingCircularList(lst,seed):
    if not isinstance(lst,list):
        lst = range(lst)
    i = 0
    random.seed(seed)
    while True:
        yield lst[i]
        if (i+1) % len(lst) ==0:
            random.shuffle(lst)
        i = (i + 1)%len(lst)

newCircle = randomizingCircularList(['a','b','c'], 10)

for i in range(10):
    print(next(newCircle))


# ### Simple classes
# 
# Here is a simple counter class:

# In[35]:


class Counter:
    """A simple counting class"""
    def __init__(self,start=0):
        """Initialize a counter to zero or start if supplied."""
        self.count= start
    def __call__(self):
        """Return the current count."""
        return self.count
    def increment(self, amount):
        """Increment the counter."""
        self.count+= amount
    def reset(self):
        """Reset the counter to zero."""
        self.count= 0


# Here\'s another simple class:

# In[36]:


class BankAccount():
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0


# Creating an instance of a BankAccount class and manipulatig the balance
# is as simple as:

# In[37]:


my_account = BankAccount(15)
my_account.withdraw(5)
print(my_account.balance)


# For most experiments you'll be creating, it's probably not necessary
# to use object oriented programming (OOP). When might you want to use it?
# Consider a dynamic experiment such as the bouncing ball (Exercise 11).
# Suppose you want to have multiple bouncing balls at the same time? This
# is cumbersome without OOP, but becomes very simple with OOP: just create
# a bouncing ball class and then instantiate a new instance of a
# bouncingBall for each one you want to appear. Remember: each class
# instance you create (e.g., `greenBall = bouncingBall(color="green")`),
# is completely independent from other instances you create.
