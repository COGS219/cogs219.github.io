#!/usr/bin/env python
# coding: utf-8

# For this activity, we will write a function that computes [the Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_number) in a few different ways.  Each number in Fibonacci Sequence is defined as the sum of the two numbers preceding it:
# 
# 0 1 1 2 3 5 8 13 21 34...
# 
# It comes up in everything from [flower petals](https://www.popmath.org.uk/rpamaths/rpampages/sunflower.html) to [rabbit populations](https://en.wikipedia.org/wiki/Fibonacci_number#/media/File:Fibonacci_Rabbits.svg)
# 
# As the numbers get larger, the ratio of a number to its predecessor, i.e., n/(n-1) approaches `phi`, the [golden ratio](https://en.wikipedia.org/wiki/Golden_ratio).

# Write a function `fibonacci()` that takes one argument `x` and returns the fibonacci sequence up to that number, e.g.,
# 
# ```python
# fibonacci(14)
# ```
# should return
# ```python
# [0, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
# ```

# In[4]:


def fibonacci(x):
    fib_so_far = [0]
    for i in range(x+1):
        if i<0:
            pass
        elif i<1:
            fib_so_far.append(1)
        else:
            fib_so_far.append(fib_so_far[-1] + fib_so_far[-2])
    return fib_so_far

print(fibonacci(14))


# In[34]:


def fib(n, fib_so_far={0: 0, 1: 1}):
    if n not in fib_so_far:
        fib_so_far[n] = fib(n-1, fib_so_far) + fib(n-2, fib_so_far)
    return fib_so_far[n]


# In[35]:


fib(5)


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


# In[7]:


def recursive_fib(x):
    if x<=0:
        pass
    elif x<=2:
        return 1
    else:
        return recursive_fib(x-1)+recursive_fib(x-2)

print(recursive_fib(9))


# In[12]:


def print_fib(n): 
  if n == 1: 
     print( "f(0) = 0" ) 
     print( "f(1) = 1" ) 
     return 0,1        
  fn_2, fn_1 = print_fib( n-1 ) 
  fn = fn_1 + fn_2 
  print( f"f({n}) = {fn}" ) 
  return fn_1, fn 

print_fib( 100 ) 


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


def is_palindrome_nonrec(str):
    if len(str)<=1:
        return True
    else:
        for i,substring in enumerate(str):
            if str[i]!=str[-i-1]:
                return False
        return True

is_palindrome_nonrec('MalayalaM')


# In[55]:


def is_palindrome_builtin(str):
    return str == str[::-1]


# In[119]:


str = '12345'
print(str[::-1])

