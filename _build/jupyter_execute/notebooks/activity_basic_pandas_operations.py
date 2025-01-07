#!/usr/bin/env python
# coding: utf-8

# # Basic Pandas Operations
# 
# ## Why do we use Pandas?
# 
# Pandas is a powerful Python library that supports creation, storage, and manipulation of data frames. Aa data-frame as a 2-dimensional data-structure -- basically a spreadsheet -- with rows and columns. It's probably the most common way that we organize our data, whether experimental, survey, whatever... It's basically the bread and butter of data-analysis.
# 
# Pandas has features such as handling missing data, cleaning up the data, and it also supports multiple file formats including CSV, Excel, SQL, etc.
# 
# In this activity, we will learn some of the basic oprations to get you started with Pandas.
# 
# ## Storing data frames in a CSV file
# 
# First we will create a dictionary containing the data. Then we can convert the dictionary to a pandas data frame and store it as a csv file. In real life you will never be hard-coding data like this. This is just a demonstration.

# In[2]:


import numpy as np
import pandas as pd

name_dict = {
    'Name':['Adam','Becky','Charlie','Daniel','Emily','Frank','Greta','Helen','Ian','Jack','Klaus','Lucy'],
    'Class ID':list(range(1,13)),
    'Age':[int(i) for i in (np.round(np.random.uniform(18,30,12),0))],
    'Score':[int(i) for i in (np.round(np.random.uniform(60,100,12),0))]
}

df = pd.DataFrame(name_dict)

df.to_csv('ClassList.csv',index=False)


# ## Loading in data from a CSV file
# 
# After loading in the data, we can do some quick checks. First, let's check the column names:

# In[28]:


df = pd.read_csv('ClassList.csv')
df.columns


# Pandas implements its own data types, but you can convert them to familiar things like lists (Basically, if it looks like it's a list, you can convert it to a list. You'll lose some functionality when you do it, but often it's functionality you don't need.).

# In[30]:


print(type(df.columns))
col_names = list(df.columns)
print(col_names)


# Next, let's look at the `head` (first few rows), and `tail` (the last few rows). This is always a good idea to make sure that everything is being read in as we expect.

# In[26]:


df.head(10) #the first 5 rows by default. If you want more, insert the number as an argument to head.


# In[24]:


df.tail() # This will give you the last 5 rows of data


# ## Accessing a particular row, column, or cell
# 
# In some cases, we want to access a particular row of the data.

# In[5]:


df.loc[0,:] # Accessing the first row of data, the first value points to the row(s) and the second value points to the column(s)


# We can select a particular column by its name

# In[6]:


df.Score # Accessing the Score column


# Or you can select a column by its index

# In[8]:


df.iloc[:,2] # This will also access the Score column


# It's also possible to select a particular cell

# In[9]:


df.iloc[0]['Score'] # This will access the first row ([0]) of the Score column


# ## Iterate through rows and access values in that row
# 
# In some cases, we need to iterate through all the rows, for example when we are using a pandas data-frame as a trial list and creating experimental trials based on that data.

# In[10]:


# Printing everything of each row
for row in df.iterrows():
    print(row)


# In[4]:


# Iterate through all rows and select only the name and Score columns
for index,row in df.iterrows():
    print(row['Name'], row['Score'])


# ## Changing data in a data-frame
# 
# If what you want to do is **change** data in a data-frame, the preferred way is to **not** iterate through the data-frame, but change it procedurally. For example, let's say we want to add a column to our data-frame that converts scores to letter-grades. Rather than iterating through it and executing various conditionals, we do this:

# In[21]:


def convert_score_to_grade(score):
    min_score_to_letter = {90:'A', 80:'B', 70:'C', 60:'D', 0:'F'}
    for min_score,letter in min_score_to_letter.items():
        if score>=min_score:
            return letter

df['Letter'] = list(map(convert_score_to_grade, df['Score'])) #create a new column called Letter

#now let's check it
for index,row in df.iterrows():
    print(row['Score'], row['Letter'])

