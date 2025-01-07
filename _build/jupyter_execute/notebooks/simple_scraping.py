#!/usr/bin/env python
# coding: utf-8

# # Simple scraping with BeautifulSoup!

# Now that you've gone through the Lynda tutorial, let's put your skills to use with a couple quick scraping exercises.   

# ## Get current temperature in Madison

# Let's programmatically get the temperature in Madison from weather.com (like in the example 
# [here](http://bdewilde.github.io/blog/blogger/2012/11/14/web-scraping-and-html-parsing-1/)). I'll start you off

# In[5]:


# -*- coding: utf-8 -*-
import re
import urllib2,sys
from bs4 import BeautifulSoup, NavigableString

weather_channel = requests.get("https://weather.com/weather/today/l/USWI0411:1:US").text
soup_weather_channel = BeautifulSoup(weather_channel)

temp = ''#something something
print temp #should print the current temperature (just the number)


# ## Get temperatures for Lake Mendota

# Going along with the temperature theme, here's a slightly more complex exercise. Let's get the current water and air temperature from Lake Mendota and compute their difference.

# In[8]:


# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup, NavigableString

mendota = requests.get("https://lter.limnology.wisc.edu/researchsite/lake-mendota").text
soup_mendota = BeautifulSoup(mendota)

water_temp = air_temp = 0

print(water_temp, air_temp, str(air_temp-water_temp)) #should print out the temperatures (in F), and the difference


# In[ ]:




