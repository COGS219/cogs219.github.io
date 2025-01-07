#!/usr/bin/env python
# coding: utf-8

# # Exercise 7 - Exploring the General Social Survey
# 
# [Accept the exercise](https://classroom.github.com/a/-_Q2eUbC)
# 
# **Due date is Wednesday at 11 for this one again. You can work in groups of 2 or individually. If you're looking for a partner, start a group whose name ends with `_team`.**  *If you'd like some extra time to submit extra credit, let me know.*
# 
# This exercise will give you practice wrangling and analyzing the general social survey. The goals are to cement the `dplyr` skills we've been working on and to give you practice going from a description of a problem to figuring out how to get the data to give you answer -- a critical skill for social science and data science.
# 
# Please [follow these instructions](https://kjhealy.github.io/gssr/) to download all the gss data and load it into R. I recommend the option using `drat` to install.  Notice that importing the data this way fixes the earlier issue we saw with numeric variables like `age` and `income` being imported as factors. So no need to do the `as.character %>% as.numeric` conversion. The factor levels remain the same, so a variable called `happy` has its largest level corresponding to a *least* happy response. Rename your variables or use `fct_rev` as necessary so that the variable name matches its values. You can see that many variables have labels built alongside to that you know what each numeric response corresponds to. 
# 
# If you want to access the label instead of the numeric response (e.g., "male" and "female" for `sex` instead of 1 and 2), load in the [labelled package](https://cran.r-project.org/web/packages/labelled/vignettes/intro_labelled.html) and use `to_factor`, e.g.
# 
# ```r
# gss$sex_l <- to_factor(gss$sex)
# ```
# 
# If you want to create factors that preserve the original order (you probably do):
# 
# ```r
# gss$sex_l <- to_factor(gss$sex, levels="p")
# ```
# `sex_l` is now a factor.
# 
# If you want to create an **ordinal** factor (you probably don't), use `ordered`:
# 
# ```r
# gss$sex_l <- to_factor(gss$sex, ordered=TRUE)
# ```
# 
# 
# Please load in all the years into a dataframe called `gss_all`. You can complete the entire exercise using this dataframe, but one of the extra credit problems asks you to also use the longitututinal "panel" dataset.

# 
# ## Part 1: Human evolution vs. elephant evolution
# 
# Recall from the GSS activity that while political orientation (`polviews`) was strongly associated with endorsement of human evolution (`evolved`), it was not strongly associated with endorsement of the evolution of elephants (`evolved2`). Visualize this interaction in the clearest way possible. Because `evolved2` was only asked in 2016 and 2018, so use the (combined) 2016 and 2018 data for this graph.
# 
# 
# ```{note}
# Earlier version asked you to plot a measure of variability. This is actually a bit tricky. If you already did, I'll give you extra credit (1 pt). Otherwise, don't worry about it
# ```

# 
# ----
# 

# ## Part 2: Basic science knowledge, politics, education, and endorsement of human evolution?
# 
# 
# Begin by creating a compound variable `science_knowledge` that contains the average correctness of the following variables:
# ```
# earthsun, electron, lasers, condrift, radioact, hotcore
# ```
# (you'll need to consult the codebook if you're not sure what the right answer is 😬)
# 
# Next, explore relationships between this variable (higher means more basic science knowledge), political affiliation (`polview` is a good one, but you can explore others), education (`degree` or `educ` for a more continuous measure), endorsement of human evolution (`evolved`)? Feel free to look at variables coding for people's employment type as well. As part of your solution for this part, report one or more main effects, an interaction (the more interesting and unexpected, the better), and a visualization that helps you gain insight into a pattern that's hard to appreciate by just looking at the numbers.
# 
# :::{tip}
# The functions `rowwise` and `mean(c_across(list_of_columns))` (or `rowMeans(across(list_of_columns))` will come in handy for creating the compound variable. See [here](https://dplyr.tidyverse.org/articles/rowwise.html) for usage examples
# :::

# ## Part 3: Sexual frequency
# 
# We're gonna talk about sex. `sexfreq` to be precise. How much and who?
# 
# a. What's the relationship between respondent's gender (`sex`) and reported sexual frequency? 
# 
# b. Is this discrepancy different for different religions (`relig`)? Note that this  question is asking about an *interaction* -- i.e., is the male vs. female difference in reported sexual frequency greater for some religions vs. others.
# 
# c. How does `sexfreq` change as a function of `year` (of survey), respondent's `age`, marital status (`marital`), and having (vs. not having) children (`childs`)? You'll want to look at combinations of these variables to get a full picture. **Good vizualizations will be very helpful here. Will be difficult to get full credit if you don't have any.** 
# 
# **Bonus:** Sexual frequency declines with age (no big surprise there). But is there some factor (location? beliefs? life factors?) that predict a substantially smaller decline?  + 2 pts
# 
# **Big Bonus** 
# Are people in some regions of the US (`region`) having more sex? You can get the averages with group_by and summarize... But that's boring. More exciting is plotting it on a map! Follow [instructions here](https://cran.r-project.org/web/packages/usmap/vignettes/mapping.html) (or a different package if you want) to plot this data on a US map. To get the mapping from GSS region names to individual states, see p. 102 of the [GSS codebook](https://gss.norc.org/Documents/codebook/GSS%202021%20Codebook.pdf). + 4 pts
# 

# ## Part 4: Tax priorities
# 
# Some people believe the government is spending too much money on certain issues. Other people believe we are not spending enough on those same issues.Explore the relationships between the following two sets of variables:
# 
# Problems:
# ```
# natspac, natenvir, natheal, natcity, natcrime, natdrug, nateduc, natrace, natarms, nataid, natfare
# ```
# Respondents' characteristics (you may choose other variables than the ones below):
# ```
# polviews, degree (or alternatively, educ), age, sex
# ```
# 
# Pick two variables from the problems category and one variable from the respondents' characteristics category that the view for the two problems are flipped for the same group of respondents (e.g., liberals think we are spending too much money on military but too little money on education, while conservatives think the opposite). 
# 
# a. Visualize the data in a way that clearly shows the pattern. 
# 
# b. Investigate whether their views have changed over the years (`year`)
# 
# ```{tip}
# You can use geom_smooth() to fit a curve across years to see how beliefs change across time. Be wary of small sample sizes though.
# ```

# ## Part 5: Astrology: beliefs, hobbies, and personalities
# 
# About a third of the GSS respondents think that astrology is at least somewhat scientific (`astrosci`). Let's explore this. This question has an extra credit component (2 pts)
# 
# 
# a. Do people who believe that astrology is scientific (`astrosci`) also more likely to read their horoscope (`astrolgy`)? If so, how much more likely?
# 
# b. What can you say about the demographics of people who read their horoscope (`astrolgy`) vs. don't read it? Is there some dimension that is especially well associated with it? (gender? age? occupation? (see `occ10`, also `indus10`). Bonus point if you discover a correlation of >.3 (or equivalent effect size).
# 
# c. Is there a relationship between people's zodiac sign (`zodiac`) and belief in astrology? Likelihood of reading their horoscope? (bit meta there...)
# 
# d. Imagine you are true believer (and an unscrupulous data scientist) trying to find data showing that there really **is** a relationship between one's [zodiac sign](https://www.allure.com/story/zodiac-sign-personality-traits-dates) and life trajectory. What's the strongest argument you can craft based on your analyses? Some variables you might find useful: `socbar` (going to bars), `helpful`, `empathy1`,  `empathy2`...  `sprtprsn` (spirituality) -- aren't Scorpios supposed to be more mysterious or something? 🤷‍♂️. You might want to check out variables related to occupation (e.g., `occ10`, life events (`divorce`), hobbies (e.g., `camping` -- note that 1993 wave had a bunch of questions related to hobbies). **Bonus +2 for a compelling graph.**
# 
# ```{note}
# Since many of these questions were only asked in some years, if you try to use data from multiple questions at once, you may end up with 0 respondents.
# ```

# ## More bonus points!
# 
#   +3 pts
# 
# Have a look at `childs` and `sibs` across years. Why is the mean of `sibs` so much larger than the mean of `childs`?  Now look at **census data** for number of children for each year (we've provided a csv called census_children.csv for you in the repository). The question census participants are answering is how many biological children under 18 are living in their household. Notice that this census average is still very different from `sibs` (and by quite a bit more than 1). Why?
# 
# ```{tip}
# Look at the questions GSS participants being asked for `childs` and `sibs`
# ```
# 
# ```{tip}
# The mean between childs and sibs differs
# ```
# 
# 
# ```{tip}
# Discrepancies between counting biological vs. adopted and step-children will only account for a small part of the discrepancy. There is something else going on? 
# ```
# 

# ## Even more bonus points
# 
# +5 pts
# 
# The gssr package allows you to get a nicely formatted version of GSS's *panel* data by loading the panel data (see [here](https://kjhealy.github.io/gssr/) and search for panel data). Unlike the regular GSS data which is cross-sectional (different people being asked for different surveys), the panel data has the same people being queried in three different year. For example, `gss_panel08_long` contains the same people (though some dropped out) who were interviewed in 2008, 2010, and 2012. `gss_panel06_long` contains the same gorup of people interviewed in 2006, 2010, and 2012.
# 
# Investigate this panel data and try to find 1-2 questions asking about attitudes (e.g., same-sex marriage, abortion, gender roles, gun ownership) where opinions between individuals did **not** change their mind even though overall attitudes (as revealed by cross-sectional analysis) **did** change in that same time span. 
# 
# 3 pts for finding a compelling case/cases; 2 pts for an effective graph showing the difference b/w cross-sectional and longitutinal data.
# 
# ```{tip}
# Make sure you're looking at change **within** participants in the panel data, not just between years. You'll need to either use firstid or filter the data to just those participants who contributed to all waves (it's ok to look at just first and last waves too)
# ```
