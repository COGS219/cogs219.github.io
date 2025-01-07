#!/usr/bin/env python
# coding: utf-8

# # Exercise 8 - Practice with regular expressions
# 
# [Accept the exercise](https://classroom.github.com/a/0sca7Fqb)
# 
# 
# We're using python's [`re`](https://docs.python.org/3/library/re.html) package for regular expressions.
# 
# **Due date is Wednesday at 11 for this one again. You can work in groups of 2 or individually. If you're looking for a partner, start a group whose name ends with `_team`.**  *If you'd like some extra time to submit extra credit, let me know.*
# 
# 
# You can complete this assignment using python's `re` library or using R's regular expressions. My suggestion is to use Python, but as they say: your mileage may vary. I will publish solutions in Python.

# 
# ## Part 1: Word matching
# 
# Write a regexp to match (and return) all words in `words` that begin and end with a vowel. To read in the word list, use the code below.
# 
# ```python
# import pandas as pd
# data = pd.read_csv('https://psych750.github.io/data/ANC-written-count_over9.txt',encoding = "ISO-8859-1",sep="\t")
# words = list(set(data['word']))
# ```
# 
# **Bonus** (2 pts):
# 
# The regexp notebook includes an example of finding words that contain the vowels aeiou, in that order. A more difficult version is to find words that contain all the letters in *any* order. Write a regexp to find words that contain all the vowels, but in *any* order.
# 
# 
# ```{note}
# The solution should be a single regexp. There should be no loops or if statements in your code
# ```
# 
# 

# 
# ## Part 2: Match `lmno` words
# 
# Write a regexp to match (and return) all words in `words` that contain the letters l, m, n, and o -- in that order, but not necessarily consecutively.  `flamingo` should match, but so should `self-monitoring` because even though the order is disrupted, it still passes the test: se`L`f-`M`o`N`it`O`ring
# 
# ```{note}
# The solution should be a single regexp. There should be no loops or if statements in your code
# ```
# 
# 

# 
# ## Part 3: Hyphenated Words
# 
# Write a function that takes a string as an argument and returns a list of all hyphenated words it contains. If the string contains no hyphenated words, the function should return `False`. A hyphenated word is of the form `someword-otherword`. Your function should work regardless of whether the words are in uppercase or lowercase.
# 
# :::{note}
# The solution should be a single regexp. There should be no loops or if statements in your code. You can use syntax like
# ```python
# return match or False
# ```
# as the return sttement for your function where `match` is the list containing your matches. If it's empty, the function will return False 
# :::
# 
# :::{tip}
# It may be helpful to use \b to find word boundaries (though it's *not* necessary). If you do, you need to prepend your regular expression with 'r' so that the string is interpreted as a "raw" string; see [more info here](https://developmentality.wordpress.com/2011/09/22/python-gotcha-word-boundaries-in-regular-expressions/). 
# :::
# 

# ## Part 4: Email validation
# 
# Write a function that takes a string as an argument and returns a list of all valid emails addresses contained in the string. If the string contains no valid emails, the function should return `False`. 
# 
# A valid email address has the form: some_alphanumeric_string@something.something (there can be multiple dots at the end e.g., `uk_education@edinburgh.ac.uk` is a valid address.
# 
# ```{note}
# Email addresses can include dashes and plus signs (`+`). They **cannot** include two @ signs or two dots in a row (name..something@domain.com should be rejected). Don't worry about *all* the possible edge-cases (because there are quite a few and accounting for all of them is way beyond the scope of this class).
# ```
# 
# ```{note}
# Again, there should be no loops or if statements in your code
# ```
# 
# ```{tip}
# Check to make sure no punctuation is included as part of the email(s) that your function returns!
# ```
# 
# 

# ## Part 5 - **Bonus** - Fix weird spacing
# 
# +3 pts
# 
# Write a function `fix_spaces()` that takes a string (of arbitrary length) as an argument and returns the string with weird spacing issues all fixed up. Some examples:
# 
# 
# `fix_spaces("The  quick    brown fox") --> "The quick brown fox"` <-- multiple spaces to single spaces
# 
# `fix_spaces("Once\t\tupon a time\n\n") --> "Once upon a time\n"` <-- tabs should be changed to (single) spaces. Multiple newlines to a single newline
# 
# `fix_spaces("This sentence has a misplaced space before the period . Beginning of next sentence.") --> "This sentence has a misplaced space before the period. Beginning of next sentence"`
# 
# `fix_spaces("Version    3.2") --> "Version 3.2"` <-- don't get tripped up by non alphanumeric characters like the dot in 3.2
# 
# ```{note}
# Solutions involving several regexps are acceptable, but there should be no loops or if statements in your code
# ```
# 
# ```{tip}
# Use re.sub()
# ```
# 
# 
