#!/usr/bin/env python
# coding: utf-8

# # A couple trial-generation activities
# 
# Before you type anything, think about how to go about solving these. Try to think of two ways. Which one is easier? Do the easy one!

# ## Exercise 1
# Write a function to create a **qusi-random** sequence of these animals
# ```python
# animals = ['dog','cat','cow','pig','mouse','hamster','elephant','zebra']
# ```
# 
# Your function should accept the list as an argument and also a length parameter which indicates how long a list to create. Check to make sure that the length is at minimum the length of the list. If it's less than that, throw an error. You might find `random.sample()` useful.
# 
# Now comes the tricky part. The sequence you generate should be randomized, but not have any animal repeating back to back.
# 
# So:
# ```python
# ['cat','dog','elephant','zebra','pig','cow','hamster','mouse','mouse','dog'] 
# ```
# is not ok because mouse repeated twice in a row, but
# 
# ```python
# ['cat','dog','elephant','zebra','pig','cow','hamster','cat','mouse','dog'] 
# ```
# is ok.
# 
# ```{tip}
# You can use list comprehension with random.choice to generate sequences of arbitrary length with replacement, e.g.,
# `random_list = [random.choice(animals) for _ in range(num_items)]`
# ```
# 

# ## Exercise 2
# 
# Now let's try something a little different. Generate a sequence of animals such that, on average, there is a some chance of a back-to-back repeat. You'll want to define a function:
# 
# `def sequence_with_repeats(lst,length,prop_back_to_back)`
# 
# If prop_back_to_back is .2 then the function will generate a random sample from `lst` that is `length` long and in which (about) 20% of the elements are back-to-back repeats. 
# 

# ## Extra credit (3 extra pts on Exercise 5) 
# 
# You can start in class if there is time and finish at home (Slack me your solution)
# 
# Now let's try the opposite. Ensure that in your sequence, the repeats are at least `min_lag` elements apart and at most `max_lag` elments apart. For example, if `min_lag` is 3 and `max_lag` is 5, then there should be a repeat every 3-5 trials. This is not a back-to-back repeat! So if you have a sequence `a, b, c, d` and there's a `min_lag` of 3 and a `max_lag` of 3, then the next element must be `a`. If `min_lag` is 3 and `max_lag` is 4, then the next element could be `a` or it could be a new element `e` in which case the following element must be `a`.
