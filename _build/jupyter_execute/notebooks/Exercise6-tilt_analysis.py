#!/usr/bin/env python
# coding: utf-8

# # Exercise 6 - Exploring the tilt adjustment data
# 
# [Accept the exercise](https://classroom.github.com/a/-WCbPg2O)
# 
# Due date is Wednesday at 11 for this one since it was posted late.
# 
# Because we'll be putting together a continuous notebook (rather than developing a program) for this exercise, there's no need to have multiple tags. I encourage you though to make regular commits as you're working on the assignment. The final commit should be tagged `Exercise_6_done` and have a single notebook called exercise_6.Rmd that has clearly titled chunks (see starter code). Insert additional chunks as you see fit. Make sure you push *all* the files in your working directory to the repository, not just the Rmd file. This will help us run your code.

# Recall that the aim of this experiment was to measure the strength of this tilt illusion. We want to know whether people are mis-estimating the tilt of the numbers and whether this mis-estimation is different for left-leaning and right-leaning numbers, and also whether it changes when the numbers are mirror-reversed so they don't really look like numbers anymore.

# ```{image} images/digitalclocks.png
# :alt: Digital Clock
# :width: 460px
# :align: center
# ```
# 
# 
# 
# 
# 

# 
# ----
# 

# ```{image} images/digitalclocks_reversed.png
# :alt: Digital Clock Reversed
# :width: 460px
# :align: center
# ```

# ## Part 1
# 
# Inside the raw_data subfolder are individual data files. Each file has a column header and is tab-delimitted. We need to read them into a single R dataframe (`dat`).  Here are two solutions; pic one. The **first solution** uses R to read in individual files and concatenate them into a common dataframe. If you want to do that, look [here](https://sparkbyexamples.com/r-programming/r-read-multiple-csv-files/). The **second solution** is to concatenate them in your shell environment (i.e., terminal) and then just read in that single file using `read.csv()`. See [here](https://psych750.github.io/notebooks/Shell_reference.html#combine-concatenate-two-or-more-files-and-write-the-output-to-another-file) for how to concatenate multiple files into one (the only very slightly tricky part is what to do about the column headers). 
# 
# For this part, submit an R notebook containing code that reads in your data file into a dataframe called `dat` **and** the data file(s) that are being read in.
# 
# 

# ## Part 2
# 
# Add a new column to `dat` called `signed_tilt`. It should be the negative of `true_angle` if `tilt_direction` is "left", and just `true_angle` if `tilt_direction` is "right", e.g.,
# 
# ```csv
#      true_angle tilt_direction signed_tilt
#           8          right           8
#          10          right          10
#          16           left         -16
#           7          right           7
#           4           left          -4
#           2           left          -2
# ```
# 
# Next, create a `exclude` column which is set to 1 if RT<600 **or** if we're on a practice trial, i.e., if `practice_or_real`=="practice"
# 
# Your `dat` dataframe should contain both of these new columns when you submit.

# ## Part 3
# 
# From now on exclude all trials for which `exclude==1` **in all calculations/graphs**. Please add code blocks to your notebook to accomplish the following 4 things:
# 
# 1. Compute the number of rows for which `exclude==0`
# 2. Compute the mean `absolute_error` for trials with true_angle<=8 and trials for which true_angle>8. Which is the bigger error? (include this as plain text, outside of the code block in your notebook)
# 3. Output the mean absolute errors for each subj_code. Which subj_code has the smallest absolute_error? Largest absolute_error (you may want to use `arrange` to sort by absolute_error).
# 4. What's the correlation between the total number of mouse wheel turns and absolute error? (you can use `cor()` to compute the correlation between two variables). 

# ## Part 4
# 
# For this part we'll just look at a subset of data: `orientation == "upright" & displayed_string == "7-44"` (as mentioned above, make sure to only include trials for which exclude==0)
# 
# Use `pivot_wider` to compute the mean difference for each subject between the `signed_error` for left vs. right tilting stimuli? Do this by creating a new column calld `left_minus_right` whose value is just that: the left error minus the right error. 
# 
# ```{tip}
# Begin by filtering for the desired orientation and displayed string. Then group by subj_code and tilt_direciton, and compute the mean signed_error for each subj_code and tilt_direction combination. Prior to running pivot_wider, the summarized data-frame should have 16 rows (8 subjects * two conditions per subject)
# ```

# ## Part 5
# 
# Generate some graphs using ggplot that help you answer the following questions:
# 
# 1. Are people reporting the tilt more accurately for 7-44 when it's tilting leftward or rightward?
# 2. Are people's tilt estimates biased differently for leftward vs. rightward tilting numbers?
# 3. Are these biases different for 7-44 shown upright vs. inverted? (coded in the `orientation` column).
# 
# :::{important}
# **Please knit your analysis Rmd file to HTML** when you submit. It makes it much easier for us to grade. Click on `knit` and choose Knit to HTML. It will then create a new .html file in your working directory.
# :::
# 
# Don't worry about plotting error bars or computing any inferential statistics. Just make some beautiful graphs! If you have an idea for the kind of graph you want, but are having trouble getting ggplot to cooperate, send a sketch of what you're trying to do on Slack and we'll help.
# 
# ```{tip}
# You'll want to average the data by subject/conditions/angles rather than feeding in raw data to ggplot
# ```
# 
# ```{tip}
# You'll probably want to generate some graphs that have `true_angle` and/or `signed_tilt` on the x-axis
# ```
# 
# :::{tip}
# You may find it useful to add [reference lines](https://ggplot2.tidyverse.org/reference/geom_abline.html) to your plot (`geom_abline` for diagonal, `geom_hline` for horizontal, `geom_vline` for vertical). 
# :::

# ## Part 6 - extra credit
# 
# For 2 points of extra credit, add a text file to your repository explaining what's funny about this post on `r/ProgrammerHumor`
# 
# 
# ```{image} images/first_name_newline.png
# :alt: Newline in name reddit post
# :align: center
# ```
# 
# 
