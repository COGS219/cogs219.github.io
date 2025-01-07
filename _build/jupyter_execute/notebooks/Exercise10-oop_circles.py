#!/usr/bin/env python
# coding: utf-8

# # Exercise 10 - Object oriented programming practice
# 
# [Accept the exercise](https://classroom.github.com/a/b4J2-QYV)
# 
# **Exercise is due Tuesday, 9pm** You can work in a team of at most 2 people. Put in _team in the team name after accepting the assignment if you are looking for a partner.
# 
# You can complete parts 1-4 either by directly editing the MovingCircles class (*not* preferred) OR creating a subclass of MovingCircles that inherit from the SuperClass and adds in your additional functionality (preferred). **If** you go with the first solution, your commits will need to include new movingcircles.py files. If you go with the second solution, then that file won't change from what's in the starting code so it doesn't need to be updated..5 be   

# 
# ## Part 1: Make it red!
# 
# Add a method `make_it_red()` such that when you click on a moving circle, it turns red. All the circles should continue moving. There should not be any pauses.
# 

# ## Part 2: Make them stop
# 
# Add a method `make_them_stop()` such that when you click on a moving circle, it keeps moving, but all the other circles stop moving.

# ## Part 3 Make it drop!
# 
# Add a method `make_it_drop()` such that when you click on a moving circle, it drops to the bottom and remains there (it's ok if it's not completely visible, but it should be a small tweak to make it visible, i.e., not go totally off-screen) The drop should be gradual -- the circle should smoothly descend down. The other circles should keep moving while the one you clicked on is dropping to the ground.
# 
# ```{tip}
# Have make_it_drop() change an attribute in the clicked-on circle so that it moves downwards.
# ```
# 

# ## Part 4: Make it drop.... more naturally
# 
# When things drop here on Earth, they don't fall at a constant velocity. They accelerate because, you know... gravity! Extend your `make_it_drop()` method to accept a parameter `accelerate`. Its default value is False. When set to True, the circle should drop as in part 3, but it should accelerate downward according to:
# 
# ```python
# h = .5*g*t**2
# ```
# :::{note}
# In Python, as in many other programming languages `**` is exponentiation, i.e, `3**3=27`
# :::
# 
# If you remember your high school physics,`g` is the gravitational constant which is 9.8 m/s/s. In our case, the units can be pixels, so 9.8 pixels per second per second.
# 
# `h` is the distance travelled (in our case, the distance from the circle's starting position, and `t`, is, of course, time. Use seconds for time. Remember that if your laptop is refreshing at 60Hz, each frame lasts ~17 msecs, i.e., .017 seconds. Refresh the position of the circle on each frame so that it's nice and smooth. The other circles should keep moving as normal when the circle you clicked on drops down. 
# 
# 

# ## Bonus 
# 
# a. (2 pts) Right now the circles are wiggling around and when they hit the wall they kind of stick around there until, by chance, they reverse course. Change the code so that the circles move in straight lines, but when they hit a wall, they bounce in a geometrically appropriate way (like [Pong](https://www.youtube.com/watch?v=fiShX2pTz9A)).
# 
# 
# b. (3 pts) Extend your code to make a little game. Position little rectangles along the bottom. These will represent enemy buildings. Now, clicking on a circle should cause it to stop moving horizontally and accelerate downwards (just like in part 4). If it hits a building, the building should turn red. When you run out of circles to click on, the game is over. If you want, put a little score in the corner that increases by 1 every time you hit a building.
# 
# ```{tip}
# You can check if a rectangle contains a point (like the position of a current circle.. hint hint) by using [Rect.contains()](https://psychopy.org/api/visual/rect.html#psychopy.visual.rect.Rect.contains)
# ```
# 
