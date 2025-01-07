#!/usr/bin/env python
# coding: utf-8

# # PRAW
# 
# ## Introduction to PRAW
# 
# `PRAW` is an API wrapper for Reddit. It lets you access Reddit content without worrying about violating Reddit's data access rules. This notebook is designed to get you going with the basics. See [here](https://praw.readthedocs.io/en/stable/) for full documentation. 
# 
# ## Installing PRAW
# 
# Within the psych750 environment, install praw using `pip`:
# 
# ```
# pip install praw
# ```
# 
# ## Working with PRAW
# We first need to create an instance of the Reddig class using an existing Reddit account. We created an account for testing purposes:

# In[19]:


import praw

r = praw.Reddit(
    client_id = 'BHpXy52FE-8za63YtAqvOQ',
    client_secret = 'GWEUpuB6M4q9YB2q9SOvY6OuGJ20JQ',
    password='psych750!Tutorial',
    user_agent = 'testscript by u/tutorial_for_praw',
    username='tutorial_for_praw'
)
print(r.user.me()) # Checking if it's working, it should just show the user name


# ## Authenticating PRAW to access Reddit
# 
# To use PRAW, you need to authenticate with your Reddit account. For your own code, you'll want to use your own account (or create a new one). First create a new Reddit account or use one you already have. Then go [here](https://www.reddit.com/prefs/apps/) and click on the `are you a developer? create an app...` button to create an application. Name it `psych750` and choose `script`. Add in a short description and use `http://localhost:8080` as the redirect uri. The usename is your regular username and the password is that user's password. The client_id string is the code in the upper-left by user_script
# 

# ## Accessing top posts
# 
# Hottest 10 posts on Reddit (as of the time of writing this tutorial).

# In[2]:


for cur_submission in r.front.hot(limit = 10):
    # print(cur_submission)
    submission = r.submission(cur_submission)
    print(submission.title)


# Let's look at one of them. [This submission](https://www.reddit.com/r/todayilearned/comments/ysm4ys/til_blacking_out_from_alcohol_doesnt_cause_you_to/) talks about how your brain temporarily loses the ability to create new memories when you experience a blackout from alcohol. It has more than 1000 comments and we can use PRAW to extract all the comments and see what people's opinions are. See [here](https://praw.readthedocs.io/en/stable/tutorials/comments.html#extracting-comments-with-praw) for info on extracting comments.
# 
# Let's take a look at the top 5 comments.

# ## Accessing comments
# 
# ### Access comments via the submission's URL
# 
# Let's acces top 5 comments of a particular submission. We can access the submission using its URL: 

# In[27]:


url = 'https://www.reddit.com/r/todayilearned/comments/ysm4ys/til_blacking_out_from_alcohol_doesnt_cause_you_to/'

submission = r.submission(url = url)

for top_level_comment in submission.comments[:5]:
    print(top_level_comment.body)


# ### Access comments via the submission's ID
# 
# Or we can access it using its unique id (let's grab the hottest comments again -- different day than the ones listed above, so they'll be different. 
# This time we'll output their titles along with their IDs and their poster's username.

# In[25]:


for cur_submission in r.front.hot(limit = 10):
    # print(cur_submission)
    submission = r.submission(cur_submission)
    print(submission.title,submission.id,submission.author,'\n')


# In[26]:


submission = r.submission(id='ywvvpv')
for top_level_comment in submission.comments[:5]:
    print(top_level_comment.body)


# ## Using NLTK to extract info from comments

# Let's use `nltk` to extract some information from these comments. It will take a little while because we're interacting in real time with the Reddit site for pulling these data.
# 
# ```{note}
# See [here](https://praw.readthedocs.io/en/stable/tutorials/comments.html#the-replace-more-method) for info on the replace_more method.
# ```

# In[11]:


import nltk

all_comments = ''
submission.comments.replace_more()
for top_level_comment in submission.comments:
    all_comments += top_level_comment.body

all_comments_tokens = nltk.word_tokenize(all_comments)
all_comments_pos = nltk.pos_tag(all_comments_tokens)


# In[14]:


all_comments_nouns = [word[0].lower() for word in all_comments_pos if word[1][:2] == 'NN']
print(nltk.FreqDist(all_comments_nouns).most_common(20))


# ## Accessing upvotes
# 
# Let's find out how many upvotes it received:

# In[15]:


print('This submission has: ' + str(submission.score) + ' upvotes!')


# What about downvotes? PRAW does not have a downvote attribute you can look up. It only has a downvote method that lets you actually downvote the submission. So don't do that unless you want to downvote it! To find the number of downvotes, we need to calculate it based on the score (number of upvotes) and the upvote ratio:

# In[16]:


print(f'This submission has: {str(round(submission.score * (1-submission.upvote_ratio)))} downvotes!')


# ## Demo of accessing most frequent nouns used in a subreddit's posts
# Let's try something else. Let's take a look at what people in Wisconsin are discussing these days.

# In[17]:


all_hot_submissions = ''
for cur_submission in r.subreddit("wisconsin").hot():
    submission = r.submission(cur_submission)
    all_hot_submissions += submission.title

all_hot_submissions_tokens = nltk.word_tokenize(all_hot_submissions)
all_hot_submissions_pos = nltk.pos_tag(all_hot_submissions_tokens)
all_hot_submissions_nouns = [word[0].lower() for word in all_hot_submissions_pos if word[1][:2] == 'NN']

print(nltk.FreqDist(all_hot_submissions_nouns).most_common(15))


# Not a big surprise, people are mostly talking about the recent election.
# 

# ## Accessing user info of hottest post 
# 

# In[23]:


for cur_submission in r.subreddit("wisconsin").hot(limit = 1):
    hottest_submission_in_wisconsin = r.submission(cur_submission)

print(f'The hottest submission in r/wisconsin is: {hottest_submission_in_wisconsin.title} by {hottest_submission_in_wisconsin.author}')


# Can we find out more about this user? What's this person's karma? Where else has this user posted within the last month?

# In[67]:


import time

user_instance = hottest_submission_in_wisconsin.author
print('this user has ' + str(user_instance.comment_karma) + ' karma!')

all_subreddits_user_posted = []
for cur_submission in user_instance.submissions.new():
    submission = r.submission(cur_submission)
    all_subreddits_user_posted.append(submission.subreddit)
    if time.time() - submission.created_utc > 60*60*24*30: #we'll walk through what's going on here in class
        break

unique_subreddits = set(all_subreddits_user_posted)
for cur_subreddit in unique_subreddits:
    print('This user has posted in ' + str(cur_subreddit.display_name) + ' in the past month.')


# We can tell that this user is a very active reddit user, probably from Madison and like dogs.
# 
# 

# ### Again with additional commentary
# 
# Let's unpack the above code a bit.
# 
# Let's grab the top posts from MadisonWI (the top post here tends to be from the moderator, so we'll go with the second highest)

# In[71]:


import time
from datetime import datetime

for cur_submission in r.subreddit("MadisonWI").top(limit = 2): 
    top_submission_in_madison = r.submission(cur_submission) #we assign the submission to a new variable

user_instance = top_submission_in_madison.author #now create a user instance from this submission

print(top_submission_in_madison.title,'||',top_submission_in_madison.author) 


# There is something a little peculiar here. If we print `top_submission_in_madison.author`, it prints as a string. But if we look at it, we see it's not a string at all:

# In[72]:


type(top_submission_in_madison.author)


# We can see that it's an object in the Redditor class. We can find out which precise methods it has by using `help(top_submission_in_madison.author)`
# but the eaier way to go is just to look at the documentation. Searching google for `praw.models.reddit.redditor.Redditor` got me [here](https://praw.readthedocs.io/en/stable/code_overview/models/redditor.html)
# 
# Now let's find this user's previous 15 posts:

# In[78]:


for num_submission,cur_submission in enumerate(user_instance.submissions.new()): #now iterate through the user's submissions
    submission = r.submission(cur_submission) # create a submission instance
    print(datetime.fromtimestamp(submission.created_utc), submission.subreddit, '||', submission.score, '||', submission.title,'\n') #access the submission's attributes: 
    if num_submission > 15: #stop after 15 submissions 
        break


# ## A joke

# In[ ]:


submission = r.submission('yshook') #the argument is the submission's id
print(submission.title)
print(submission.selftext)

