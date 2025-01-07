#!/usr/bin/env python
# coding: utf-8

# In[ ]:


You all


# In[23]:


def non_recursive_fib(x):
    fib_so_far = []
    for i in range(x+1):
        if i<=0:
            pass
        elif i<=2:
            fib_so_far.append(1)
        else:
            fib_so_far.append(fib_so_far[-1] + fib_so_far[-2])
    return fib_so_far

fib_seq = non_recursive_fib(1000)


# In[29]:


def recursive_fib(x):
    if x<=0:
        pass
    elif x<=2:
        return 1
    else:
        return recursive_fib(x-1)+recursive_fib(x-2)

fib_seq = recursive_fib(100)
print(fib_seq)


# In[24]:


fib_seq[-1]/fib_seq[-2]


# In[115]:


def is_palindrome_rec(str):
    if len(str)<=1:
        return True
    elif str[0]!=str[-1]:
        return False
    else:
        return is_palindrome_rec(str[1:-1])

is_palindrome_rec('MalayalaM')


# In[118]:


def is_palindrome_iterate(str):
    if len(str)<=1:
        return True
    else:
        for i,substring in enumerate(str):
            if str[i]!=str[-i-1]:
                return False
        return True

is_palindrome_nonrec('MalayalaM')


# In[120]:


def is_palindrome_builtin(str):
    return str == str[::-1]


# In[119]:


str = '12345'
print(str[::-1])

