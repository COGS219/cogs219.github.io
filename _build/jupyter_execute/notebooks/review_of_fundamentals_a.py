#!/usr/bin/env python
# coding: utf-8

# # Review of fundamentals A
# In this notebook, you will guess the output of simple Python statements. You should be able to correctly predict almost all (ideally *all*) of them. If you get something wrong, make sure you understand why! Don't be satisfied until you've understood why every snippet of code returns the value it does or produces the error it does.

# ## Simple operations

# In[3]:


3 + 10


# In[4]:


3 = 10


# In[5]:


3 == 10


# In[6]:


3 ** 10


# In[7]:


'3 + 10'


# In[8]:


3 * '10'


# In[9]:


a*10


# In[10]:


'a' * 10


# In[11]:


int('3') + int('10')


# In[12]:


int('hello world')


# In[13]:


10 / 5


# In[14]:


10 / 4


# In[15]:


float(10 / 4)


# In[16]:


float(10)/4


# In[17]:


type("True")


# In[18]:


type(True)


# ## Conditionals

# In[19]:


a=3
if (a==3):
    print("it's a three!")


# In[20]:


a=3
if a==3:
    print("it's a four!")


# In[21]:


a=3
if a=4:
    print( "it's a four!")
    


# In[22]:


a=3
if a<10:
    print ("we're here")
elif a<100:
    print( "and also here")
    


# In[23]:


a=3
if a<10:
    print("we're here")
if a<100:
    print("and also here")
    


# In[24]:


a = "True"
if a:
    print ("we're in the 'if'")
else:
    print ("we're in the else")


# In[3]:


a = "False"
if a:
    print("we're in the 'if'")
else:
    print("we're in the 'else'")


# ```{tip}
# If you were surprised by that, think about the difference between the literal `False` and the string `"False"`
# ```

# In[5]:


a = 5
b = 10
if a and b:
    print("a is", a)
    print("b is", b)


# ## Lists

# In[5]:


animals= ['dog', 'cat', 'panda']
if panda in animals:
    print("found it!")


# In[2]:


animals= ['dog', 'cat', 'panda']
if "panda" or "giraffe" in animals:
    print("found it!")


# In[6]:


animals= ['dog', 'cat', 'panda']
if "panda" and "giraffe" in animals:
    print("found it!")


# In[3]:


if ["dog", "cat"] in animals:
    print ("we're here")


# In[4]:


some_nums = range(1,10)
print(list(some_nums))
print(some_nums[0])


# In[14]:


animals= ['dog', 'cat', 'panda']
print(animals[-1])


# In[34]:


animals= ['dog', 'cat', 'panda']
print(animals.index('cat'))


# In[16]:


animals= ['dog', 'cat', 'panda']
more_animals = animals+['giraffe']
print (more_animals)


# In[2]:


animals= ['dog', 'cat', 'panda']
more_animals = animals.append('giraffe')
print (more_animals)


# ```{note}
# The above is a tricky one! The issue is that append() does not return a value. It simply appends.
# ```

# Compare the above with what happens in the code below

# In[3]:


animals= ['dog', 'cat', 'panda']
animals.append("giraffe")
print(animals)


# In[4]:


animals= ['dog', 'cat', 'panda']
for num,animal in enumerate(animals):
    print(f"Number {num+1} is {animals}")


# In[18]:


animals= ['dog', 'cat', 'panda']
for num,animal in enumerate(animals):
    print(f"Number {num} is {animal}")
print(f"\nWe have {len(animals)} animals in our list.")


# In[5]:


animals= ['dog', 'cat', 'panda']
while animals:
    print (animals.pop())

print(f"\nWe have {len(animals)} animals in our list")

