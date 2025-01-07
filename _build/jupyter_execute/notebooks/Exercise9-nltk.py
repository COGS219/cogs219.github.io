#!/usr/bin/env python
# coding: utf-8

# # Exercise 9 - Natural Language Processing with NLTK
# 
# [Accept the exercise](https://classroom.github.com/a/H4nxvd84)
# 
# 
# **I'll keep the due date Wednesday at 11. Don't wait until Tuesday to start though! This is a shorter assignment and you'll need to work individually on this one. There will be few bonus problems as well**
# 

# 
# ## Part 1: Who likes which adjectives?
# 
# Begin by looking over [this example](https://realpython.com/nltk-nlp-python/#tagging-parts-of-speech) of part of speech tagging.
# 
# Let's compare the adjectives used in Jane Austen's Emma to those used in Shakespeare's Hamlet.
# 
# Retrieve the two texts from `nltk.corpus.gutenberg` ('austen-emma.txt', 'shakespeare-hamlet'), tokenize the text. Do not lowercase or remove punctuations until **after** you get the part of speech tags. 
# 
# You'll want to keep the two books in separate variables -- `emma` and `hamlet`.
# 
# Now use [`nltk.pos_tag`](https://www.nltk.org/_modules/nltk/tag.html) to infer the part of speech of each word.  This will allow you to pull out all the adjectives. Print the list of the 15 most common adjectives for Emma and the 15 most common for Hamlet. 
# 
# ```{note}
# nltk's pos_tag tagger is trained on Penn's treebank. There are more sophisticated neural-net based taggers available such as [FLAIR](https://github.com/flairNLP/flair)
# ```
# 

# ## Part 2: Increasing robustness
# 
# Let's see if the analysis for part 1 holds up when we add some additional books for these authors. Repeat what you did for part 1, but now add 2 more books to the `austen` corpus and 2 additional plays to the `shakespeare` corpus:
# 
# The first corpus -- `austen`-- should contain three Jane Austen books:
# ```csv
# ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt']
# ```
# 
# The second corpus -- `shakespeare` -- should contain three Shakespeare plays:
# ```csv
# ['shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt']
# ```
# 
# How do the 15 most popular adjecives look now? 

# ## Part 3 - Comparing verb lemmas
# 
# Let's now compare verbs in `austen` and `shakespeare`. 
# 
# a. Print out the 15 most frequent verbs in each corpus (after removing stopwords).
# 
# b. **Lemmatize** the corpus and print out the 15 most frequent verb lemmas after removing stopwords. You will need to tag parts of speech first, and then feed them into the lemmatizer to lemmatize correctly.
# 
# ```{note}
# The stopwords are used by the part-of-speech to guess the parts of speech so make sure the text you feed into it has them! Remove stopwords as the very last part of your workflow
# ```
# 
# :::{tip}
# There are many lemmatizers. The basic one in NLTK is `WordNetLemmatizer`. Notice that its parts of speech tags are not the same as what's outputted by the part of speech tagger, so you'll need to map between them. There are some examples of other lemmatizers in action [here](https://www.machinelearningplus.com/nlp/lemmatization-examples-python/).
# :::

# ## Bonus problem - US vs. UK English
# 
# ### Part a. (3 pts)
# Inside the [starter code repo](https://github.com/psych750/exercise_9) is a directory `data_for_bonus` which contains two english corpora, one is US English, the other is British English. If you've already accepted the exercise, you'll need to pull from the repository to get this additional data.
# 
# Add in the following to your import statements:
# ```python
# from nltk import collocations, FreqDist, bigrams, trigrams
# trigram_measures = nltk.collocations.TrigramAssocMeasures()
# ```
# 
# Read in the us and uk corpus data into separate variables, tokenize it (its already lowercased), and get rid of the stopwords.
# 
# 
# Print out the top 20 trigram-based collocations in US and UK English. Get the collocations using `TrigramCollocationFinder` and rank them using the likelihood_ratio measure, one of the trigram measures (look at `trigram_measures` defined above). You can use the `nbest` method from `nltk.TrigramCollocationFinder()` to print the top n collocations
# 
# ```{note}
# The question asks about likely collocations, not just frequent trigrams
# ```
# 
# ```{note}
# It will take quite a while (a few minutes!) to get rid of the stop words in these ~1M token corpora. This is ages in computer time. The reason it takes so long is that the typical solution -- check each word against the list of stop words is wildly inefficient. Part b of the bonus asks you to implement a more efficient solution
# ```
# 
# ### Part b. (3 pts)
# 
# Change how you remove stopwords from the corpus so that it takes a few seconds rather than a few minutes (2 pts)
# 
# Explain why the new solution is so much faster (1 pt)
# 
# ```{note}
# You can get credit for a correct explanation if you can't figure out a way to implement it
# ```
