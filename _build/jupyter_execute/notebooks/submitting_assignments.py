#!/usr/bin/env python
# coding: utf-8

# # Submitting assignments
# 
# We'll be using Github classroom for submitting assignments. This will give you practice with version control and allow us to easily comment on your code. 
# 
# **Assignments are due on Tuesday by 9pm central.**

# ## Step 1: Accept an assignment
# 
# 1. Make sure git is installed and that you have an account on Github (see installation instructions)
# 2. Accept the assignment. For the purposes of this tutorial, please accept [this test assignment](https://classroom.github.com/a/kptjb8LU)
# 3. Next, you'll want to clone the repository on your local machine using 
#     ```bash
#     git clone URL
#     ```
#     where URL is the URL of your personal assignment repository; it should look something like https://github.com/psych750/exercise-0-glupyan
#     ```{tip}
#     Use a directory like Documents/classes/psych750/exercises and clone all the exercises into it to keep things neat
#     ```
# 
#     ```{note}
#     We recommend **not** using the "Open in VSCode" option and **not** attempting to do git commits within VSCode unless you know what you're doing -- this can change the directory structure and cause hard-to-debug issues with submitting your assignments. 
#     ```
# 
# 

# ## Step 2: Do the assignment
# 
# Note that your cloned repository (The test assignment called Exercise_0) contains a file called `test_assignment.py`. For real assignments, the exercise repository will contain starter code and any additional files you may need to complete the assignment.
# 
# This test assignment has 3 parts: 
# 1. Create a new file called `my_addition.txt` which should just have the text "A new file" 
# 2. Edit `my_addition.txt` to have a second line of text reading "I added a second line"
# 3. Edit `test_assignment.py` to print `Hello big world`
# 
# When you're done with each part, you're going to commit the change, tag it, and push it to the remote repository allowing us to look at it and give you feedback as necessary.

# ## Step 3: Submit each part of the assignment
# 
# After you complete each part, commit the changes and tag it.  Here's the workflow.
# 
# ```bash
# git add .
# git commit -m "Finished part 1"
# git tag "Exercise_0_1"
# git push origin main --tags
# ```
# 
# Let's break this down:
# 
# `git add` tells git that you want to "stage" the files for committing. The dot is a wildcard meaning all the files in the directory and all the directories within it. (`git add *`) means stage all the files in the current directory. `git add <filename>` would stage just the specific file you specify. 
# 
# The next line - `git commit` Commits the changes and the message tells others (or the future you) what happened during this commit. 
# 
# Each commit is identified by a unique identifier composed of a bunch of letters and numbers. Not very meaningful. `git tag` allows you to tag the commit with an informative and easy to type name
# 
# :::{important}
# Be mindful of capitalization. Git commands (like most programming environments) are case-sensitive. `exercise_1_1` and `Exercise_1_1` are completely different strings. Also be mindful of things like *smartquotes*--those nice looking quotes that word-processors (and keyboards with some language-settings) might insert in place of plainquotes. `""` (plainquotes) are different from `“”` (smart-quotes). In all cases, use plainquotes.
# :::
# 
# 
# Ginally, `git push` pushes the commit (and the associated tags) to the remote repository. You don't need to push after every commit. You can make make commits, tag them, keep working and then push the whole thing when you're done. Obviously, if you would like us to look at your code in your repository, you'll need to push first.
# 
# ```{important}
# The first time you push, you may be asked to valiate your github access token. If you have trouble with this, ask for help.  
# ```
# 
# Some parts of actual assignments will require you to code quite a bit, so you'll want to make multiple commits. You can push these intermediate commits to the classroom site if you like, but all that's required is that your final solution for each part is committed **and tagged**. 
# 
# :::{important}
# You must use following format for tags: `Exercise_[exercise#]_[part#]`. For example, your tag for part 3 of Exercise 2 should be `Exercise_2_3`. Please make sure this is correct!
# :::
# 
# ```{tip}
# After you've tracked the file you are changing with `git add .` You can combine `add` and `commit` into a single line like so: `git commit -am "Finished part 2"`.
# ```
# 
# ```{note}
# By default, `git tag` will assign the tag to your most recent commit (i.e., the [HEAD](https://initialcommit.com/blog/what-is-git-head#:~:text=In%20Git%2C%20a%20head%20is,recent%20commit)). 
# 
# If you want to attach the tag to a previous version, you can do specify its unique code(hash; see Tips below). You can read more about tags [here](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
# ```
# 
# ```{warning}
# Forgetting to use `--tags`` after `push` will cause the tags you added to only be visible to you locally; we won't be able to see them on our end
# ```

# # Looking at solutions
# 
# Following the submission deadline, I will push the Exercise solutions to a private repository https://github.com/psych750/solution
# You must be subscribed to this repository., 
# They will be tagged in the same way as your submitted assignments so you can browse the tags on the github site or `checkout` individual tagged commits using `git checkout`

# #  Tips
# 
# ## See the git log
# ```bash
# git log
# ```
# 
# You can print a more compact log using
# ```bash
# git log --oneline
# ```
# 
# 
# `git log` will list the commits made on the branch you're currently on. If you want to also see the commits you made while on other branches, use 
# 
# ```bash
# git log --all
# ```
# Or combine it with --oneline for more compact printing. 
# 
# If you want to additionally see the commits made on unnamed (typically temporary) branches, you can with this:
# ```bash
# git log --reflog
# ```
# 
# ## Figure out what's been changed and which files are being staged
# ```bash
# git status
# ```
# 
# ## Check out a particular commit 
# 
# You can check out using a tag name, e.g., `Exercise_1_2`
# ```bash
# git checkout <tag name>
# ```
# You can list the available tags (i.e., those you've used previously) with
# ```bash
# git tag
# ```
# 
# If you want to go to a previous commit that did not have a tag associated with it, use the hash provided by `git log` use the hash value of the commit you want to revert to:
# 
# 
# 
# e.g. if the relevant part of the log looks like this:
# ![images/git_log_example.jpg](images/git_log_example.jpg)
# 
# you can go to this commit by using 
# ```bash
# git checkout 6ebc972579c733621124e40360812777aeeeeb6f
# ```
# 
# ## Undo a push
# 
# Sometimes you'll push some changes to a remote repository and want to undo them.  To do this, reset back to the version you want by using the appropriate hash, e.g.
# 
# ```bash
# git reset --hard a4711f034e8cf4d90a4e537428b033333240d58a
# ```
# 
# ```{note}
# The --hard flag ensures that the reverted commit is wiped clean from the git log 
# ```
# 
# This resets your local branch. You can now update the remote branch to the current status (the current HEAD) by using
# ```bash
# git push -f
# ```
# 
# 
# ## Get the URL of remote branch
# ```bash
# git remote -v
# ```
# 
# ## Change where a repository pushes to
# In case you need to change the URL that you are pushing to
# ```bash
# git remote set-url origin https://some_url/some_repo
# ```
# `origin` is just a convention for naming the original URL that you first cloned from
# 
# ## List the available branches
# Lists both local and remote branches
# ```bash
# git branch -a
# ```
# 
# ## Switch to a particular branch
# ```bash
# git switch <branchname>
# ```
# 
# ## Delete tags
# Sometimes you might want to delete a local and/or remote tag. Because you can't have two identical tags, if you want to update info associated with a particular tag, you first need to delete the tag and then tag (to local) or push (to remote) the new tag.
# 
# ### Deleting a remote tag
# ```bash
# git push --delete origin "name of your tag"
# ```
# 
# ### Deleting a local tag
# ```bash
# git tag -d "name of your tag"
# ```
# 
# ### Deleting multiple tags at once
# [Here's a discussion](https://gist.github.com/shsteimer/7257245) of various ways to delete multiple tags at once based on pattern matching, e.g., delete all tags beginning with `Exercise_1_` 
# 
# ## Detached HEAD?
# 
# Do you have a detached HEAD that you want to re-attach? [See here](https://stackoverflow.com/questions/10228760/how-do-i-fix-a-git-detached-head) 
