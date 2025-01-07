#!/usr/bin/env python
# coding: utf-8

# # Let's warm up them neurons
# 

# Now that we've gotten your environment all set up, let's switch gears and do some actual coding.

# 1. Write a `for` loop to print out the numbers 0 through 5
# 2. Write a `for` loop to print out the numbers 2 through 8. Now do another one to print 9 through 0 (i.e., backwards)
#      :::{tip}
#      Use help(range) to see some other things you can do with the range function
#      :::
# 3. Write a bit of code using `for` loop(s) that prints out the following sequence:
#      :::
#      1
#      12
#      123
#      1234
#      12345
#      :::
# 
#      :::{note}
#      This one's may be challenging to people who have not programmed before. Give it a try on your own. If you're having trouble, turn to your neighbor and talk about how to solve it.
#      :::
#      :::{tip}
#      Python will automatically start every separate `print()` statement on a new line. If you want to have several separate print statements print all to the same line, include an `end=""` argument in your print statement, e.g.: 
#      ```python
#      print("I'm gonna print on line 1",end="")
#      print("And so will I")
#      >>> I'm gonna print on line 1And so will I
#      ```
#      You can print a single newline, do this:
#      ```python
#      print('\n',end="")
#      ``` 
#      :::
# 4. If you've done any coding before, the last one was probably quite easy. Here's one that's slightly more challenging: Write some code that uses a variable `rows` to print the following: 
# If `row==1`, then the following pattern should be printed:
# :::
# o
# :::
# 
# If `rows==5`, then the following pattern should be printed.
# 
# :::
#      o
#     ooo
#    ooooo
#   ooooooo
#  ooooooooo
# :::
# 
# You should be able to give any value to row (though at some point you will run out screen space for printing). Before you start coding, **think** what set of instructions (algorithm) your code needs to carry out for a certain value of `rows`. 
# 
# 
# If it doesn't look like a pyramid, you're not doing it right ;)
# 
