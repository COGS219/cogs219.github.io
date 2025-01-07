#!/usr/bin/env python
# coding: utf-8

# # Primer on writing files
# 
# Your programs become a whole lot more useful when you are able to access external data (typically from external files) and when you can save your outputs (participant responses, outputs of your computations, etc.) to files.
# 
# We'll do lots of reading from files in the coming weeks. This primer is for providing you with the minimum information necessary to write to files that you'll need to complete Exercise 2.
# 
# 
# ## How to open a file for writing?
# 
# ```python
# output_file = open('results.csv','w')
# ```
# 
# Here, we've opened a file called results.csv. The 'w' flag tells Python to open the file in writing mode. The open() function outputs a "file handle" that we assign to a variable, here called `output_file`. This variable then allows you to write new data to the file.
# 
# ```{warning}
# If you open() results.txt and it already exists, it will be overwritten (i.e., all existing data in results.txt will be lost)
# ```
# 
# ## How to write to a file?
# 
# Once a file is open for writing, you can write to it like so:
# 
# ```python
# output_file.write('Hello, world!')
# ```
# 
# When you are completely done writing and want to close the file (so that it's not corrupted by other processes that may write to it), close it like so:
# 
# ```python
# output_file.close()
# ```
# 
# Remember, don't close it until you are totally done. If you reopen it in 'w' mode, it will be rewritten (we'll talk later about **appending** to files, but this is not necessary for Exercise 2).
# 
# ```{note}
# When you write to a file you have to be mindful of newlines. If you want to write separate lines, you need to explicitly add a "\n" character to your string.
# ```
# 
# 

# ## Practice writing to files
# 
# 1. Open a file called 'counter.txt' and write the following list to it, one word (element) at a time
#     ```python
#     list_to_write = ['one','two','three','four','five']
#     ```
# 2. Open a file called 'results.csv' and write code so that at the end the file looks like this. Make sure you code can accommodate a list of arbitrary length. If I asked you to write 50 lines, your code should be no longer than for printing these 4.
#     ```csv
#     1,dog
#     2,cat
#     3,wolf
#     4,penguin
#     ```
