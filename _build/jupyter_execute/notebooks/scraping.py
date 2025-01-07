#!/usr/bin/env python
# coding: utf-8

# # Webscraping with Beautiful Soup
# 
# This notebook shows off some basic capabilities. of the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) webscraping package. And here's a handy [cheat sheet](https://whatacold.io/blog/2021-12-05-beautifulsoup4-cheatsheet/).
# 
# 
# Why Beautiful Soup? If you [google it](https://groups.google.com/g/beautifulsoup/c/nCOB_U4HqRc?pli=1), you'll be told that it's because of "tag soup" or some such nonsense. But here's a [hint](https://www.crummy.com/software/BeautifulSoup/). See that picture? That's your [answer](https://www.youtube.com/watch?v=FWxFsJUlBbw).
# 

# ## Get heading names in a Wikipedia article
# 
# Let's begin by automatically grabbing The Simpsons character names from the *Simpson Family* [Wikipedia page](https://en.wikipedia.org/wiki/Simpson_family). Looking at the wiki article, we see that the character names are part of a bulleted list (produced by the html `<ul>` tag. Furthermore, they're bolded. Using this we can do the following:

# In[118]:


from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Simpson_family"
r = requests.get(url)
soup = BeautifulSoup(r.content)

for headline in soup('span', attrs={'class' : 'mw-headline'}):
    topics = headline.find_next('ul').find_all('b') #ul is bulletpoints; b is bold
    for topic in topics:
        print ('*', topic.text)


# There are some false alarms, but it works pretty well! You might wonder whether this is too much trouble to go through just to get the Simpsons characters. But of course the identical code will work on pretty much *any* wiki article. ...an the approach can be used on any webpage. And that's really the point.

# ## Get current temperature in Madison
# 
# Let's look at another example showing how we can grab a particular piece of information from a webpage: the current temperature. I'll walk you through what's going on here in class.
# 

# In[120]:


soup = BeautifulSoup(requests.get("https://weather.com/weather/today/l/USWI0411:1:US").text)
results= soup.find_all('span', attrs={'class': 'CurrentConditions--tempValue--MHmYY'})
print (results[0].getText())


# (This is about as simple as it gets). This approach scales (and that's the point!). If we want to get the temperature of a 100 different cities, just load the appropriate URLs and iterate through them.

# ## Example of using the newspaper package
# 
# There's an enormous infrastructure for web scraping with lots of codebases for common tasks, e.g., scraping [newspapers3k](https://newspaper.readthedocs.io/en/latest/) for scraping online news. Let's do a quick demo of this one.
# 
# 
# First install the package using `pip newspaper3k`

# In[121]:


from newspaper import Article

url = "https://www.cnn.com/2022/11/30/world/black-hole-devours-star-scn/index.html"
article = Article(url)
article.download()
print(article)
article.parse()
print(article.authors)
print(article.publish_date)
print(article.text[:1000]) #first 1000 chars



# We can also grab images associated with it. Let's grab the URL of the head image and then download it.

# In[110]:


import urllib
from IPython import display

print(article.top_image)
raw_img = urllib.request.urlopen(article.top_image).read()
#display.Image(raw_img) # this will work when you render the notebook locally, but not when it's uploaded to github as we do here




# 
# ![top_image](https://media.cnn.com/api/v1/images/stellar/prod/221130121224-01-black-hole-tidal-disruption-event.jpg)

# ## Lots of examples and pre-written code out there!
# 
# Here's a nice step by step tutorial  example of a script that uses BeautifulSoup to [scrape data from google scholar](https://proxiesapi-com.medium.com/scraping-google-scholar-with-python-and-beautifulsoup-850cbdfedbcf).
# 
# For an especially creative example of scraping, check out [this blog post by Erik Bern](https://erikbern.com/2017/02/01/language-pitch.html) which bulk downloads pronunciations of words in various languages to examine whether there are consistent differences in pitch (fundamental frequency) between languages (Sounds like Finnish is Lowwww).
# 
# 

# ## Now it's your turn

# * Get the current water temperature in Malta, displayed here:
# `https://seatemperature.net/current/malta/valletta-il-belt-valletta-malta-sea-temperature`

# * Now a trickier one -- get the displayed temperature from a week ago, displayed just to the right of the current temperature.
# 
# ```{tip}
# Use the `children` method to iterate through the "children" of the id containing the info you need.
# ```

# In[122]:


soup = BeautifulSoup(requests.get("https://seatemperature.net/current/malta/valletta-il-belt-valletta-malta-sea-temperature").text)

results = soup.find_all(id='temp2')
for cur_result in results:
    para = cur_result.find_all('p')
    for cur_para in para:
        print(cur_para.getText())


# In[124]:


results = soup.find_all(id='temp2')

children = list(results[0].children)
#print(children)
print(children[1].getText().split(':')[1].replace(' ',''))


# * Let's do another one.
# 
# Here's an example of scraping the Billboard 100 site

# In[125]:


page = requests.get('https://www.billboard.com/charts/year-end/hot-100-songs/')
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('h3', attrs={'class': 'c-title'})
for placement, result in enumerate(results):
    print(placement+1,result.getText().strip())
    if placement+1>=100: #avoids some junk at the end
        break


# Can you figure out how to get the **artists** instead?

# In[128]:


page = requests.get('https://www.billboard.com/charts/year-end/hot-100-songs/')
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('span', attrs={'class' : 'c-label'})
for cur_result in results:
    sub_result = cur_result.find_all('span', attrs={'class': 'a-font-primary-s'})
    print(sub_result[0].getText())

