#!/usr/bin/env python
# coding: utf-8

# # Python essentials to get you started
# 
# This notebook is designed to familiarize you with some basic programming constructs before the start of actual instruction. If you've coded before, this will show you how stuff you already know are implemented in the Python programming language. If you've never coded before, you'll probably be a bit confused. Don't worry! The class hasn't started yet!

# ## Variable types and assignments

# Variables are the building blocks of programs. You tell a compute what to do largely by maniulating the values of variables. Variables come in different types such as `string`, `integer`, `boolean`, and `float`. Because Python is what's called a dynamically typed language, you don't have to declare the type of variable before assigning a value to it. For example, let's look at these 6 (very badly named) variables.

# In[4]:


var_1 = "five"
var_2 = 5
var_3 = "5"
var_4 = 5.0
var_5 = True
var_6 = "True"


# Now let's print them out

# In[26]:


print('var_1 = ',var_1)
print('var_2 = ',var_2)
print('var_3 = ',var_3)
print('var_4 = ',var_4)
print('var_5 = ',var_5)
print('var_6 = ',var_6)


# Now let's print out the **types** of variables these are:

# In[25]:


print('var_1 = ',type(var_1))
print('var_2 = ',type(var_2))
print('var_3 = ',type(var_3))
print('var_4 = ',type(var_4))
print('var_5 = ',type(var_5))
print('var_6 = ',type(var_6))


# Notice that `var_2` and `var_3` have exactly the same printed value (5). `var_5` and `var_6` also have the same value (True). In both cases, however, they are of different types, e.g., `var_2` is an integer while `var_3` is a string; `var_5` is a boolean while `var_6` is a string.
# 
# Does this matter? Yes it does! Have a look at what happens when we try to add 3 to `var_2` vs. `var_3`

# In[5]:


print("Adding 3 to var_2 gets us ", var_2+3)
print("Adding 3 to var_3 gets us ", var_3+3)


# The first one is 8 because. 5+3=8. 
# 
# The second one throws a TypeError because you tried to combine two types (a string and an integer) in a way that could not be resolved. The string '5' + the integer 3 is not defined. Computers are literal-minded. Just because something looks like the number 5 doesn't make it a five! 
# 
# ```{note}
# You will be seeing a lot of error messages like the one above. Don't let them intimidate you. Generally, the very last line will tell you what kind of error it is (in this case, a TypeError meaning that something went wrong when combining different variable types). The text above tells you where in your code the error is coming from.
# ```

# Now have a look at this. Try to predict what happens before looking at the output

# In[33]:


print(var_3+'3')


# What happened here?! The Python interpreter was asked to add the string '3' to the string '5'. A human is cognizant that these are numbers, but the Python interpreter doesn't care. To it, these are just text strings. What's a reasonable thing to do when asked to add two strings? Python defines string addition as **concatenation**, i.e.,`string1a+string2=string1string2`. That's why we get `52` (which is itself a string!!) as the answer.
# 
# So, in the context of numbers (integers and floats) `+` is arithmetic addition. In the context of strings, it's concatenation. This is called [operator overloading](https://www.geeksforgeeks.org/operator-overloading-in-python/)

# Now let's try this one. Let's *multiply* `var_2` and `var_3` by 3. What do you think will happen?

# In[35]:


print(var_2*3)
print(var_3*3)


# ## A bit more about printing

# Although printing is not something we'll be doing much of as an end in itself, it's massively useful for debugging your code, i.e., for knowing what a value of vertain variables is at a certain point in your code. We'll talk more about this when we discuss debugging. 
# 
# When you print, Python will try to convert what you are printing to a string. But if you try to print several different data types or combine the printing of strings and variables -- both of which is something you'll be doing a lot of when debugging -- it gets cumbersome. Observe:

# Simple enough:

# In[1]:


name = "George's dog"


# But what about this?

# In[3]:


name = "George"
print(name+"'s "+"dog")


# Yuck... that's a lot of quotes and figuring out where the spaces should go. 

# Python 3 provides a bit of "syntactic sugar" for printing combinations of raw strings and variables of different types:

# In[7]:


name = "George"
print(f"{name}'s dog")


# To use so-called f strings (f stands for formatted) just encase the variables in curly-braces and write out the regular text part of the string as normal. Read more about these f-strings [here](https://realpython.com/python-f-strings/)

# ## Lists and `for` loops  

# A data structure you'll be using a whole lot in Python is a [list](https://learnpython.com/blog/python-array-vs-list/). For those coming from other programming languages, lists are largely the same as arrays, although Python lists can mix different types of variables. For example:

# In[37]:


a_list = [1, '1', 'two', 'three', 4]
print(a_list)
print(a_list[0], 'is a', type(a_list[0]))


# A common way of iterating through lists is by using a `for` loop. 

# In[38]:


animals = ['dog', 'cat', 'pig']
for animal in animals:
    print(animal)


# A common use of `for` loops is to do something a certain number of times. For example, let's print the first 10 integers, beginning from 0:

# In[9]:


for cur_num in range(10):
    print(cur_num)


# ```{dropdown} What happened here?
# `range()` generated a list of numbers in the specified range, beginning from 0. Then `for` iterates through those numbers, printing the value of each.
# ```

# You don't have to start at 0. Pass a starting number to `range()` like so.

# In[1]:


for cur_num in range (5,10):
    print(cur_num)


# ```{note}
# Technically range() returns a `range object` which is a ["lazy iterable"](https://treyhunner.com/2018/02/python-range-is-not-an-iterator/) and is executed only later, when we try to access its values. This is different from Python 2 where `range()` returns a regular list.
# ```

# What about counting by 2s or counting down? Simple

# In[2]:


for cur_num in range(0,10,2):
    print(cur_num)


# In[3]:


for cur_num in range(10,0,-1):
    print(cur_num)


# :::{tip}
# If all you need to do is to execute some command a certain number of times, there's a Python convention to use `_` as a throwaway index variable, for example, let's generate 5 random integers between 1-10:
# ```python
# import random
# for _ in range(25):
#     print(random.randrange(1,10+1))
# ```
# :::

# ## A `while` loop

# Another kind of loop we'll use is a `while` loop. We use this to iterate until a condition is met (i.e., something that's `false` becomes `true`), or a condition is no longer met (i.e., something that's `true` becomes `false`).

# In[41]:


another_num=5
while another_num>0:
    print(f"I'm a {another_num} and I'm greater than 0!")
    another_num -= 1


# ```{dropdown} What happened here?
# The first line of the while loop evaluates the truth value of another_num being greater than 0. As long as both of these conditions are met, we execute the loop. On each iteration, we decrease the value of another_num by 1 until it's no longer greater than 0 at which point the while loop exits.
# ```

# In[42]:


s = ""
while len(s)<10: 
    s+="z"
    print(s)


# ```{note}
# `+=` is shorthand for add and self-assign, i.e., 
# s+="z" is equivalent to s = s+"z"
# ```

# ## Primer on conditionals (`if` statements)

# In[7]:


my_num = 5

if my_num == 5:
    print("it's a 5!")
else:
    print("it's not a 5!")


# In[6]:


if 5<2:
    print('yes indeed')
elif 10<2:
    print('this is true too!')


# Predict what each of these statements will return. Then check.

# In[61]:


my_num = '5'
if my_num == 5:
    print("it's a 5!")
else:
    print("it's not a 5!")


# In[13]:


print('s'==True)


# In[12]:


print(1==True)


# In[11]:


print (0==True)


# In[10]:


print (True==False)


# In[9]:


print ((True or False)==True)


# Let's end with a weird one...

# In[6]:


if print==True or print==False:
    print('all is good')
else:
    print('uh oh')


# In[9]:


print(type(print))
print(print==True)
print(print==False)

