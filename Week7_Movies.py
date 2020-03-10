#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv(r'C:\Users\shani\Downloads\movies.csv')
df.head()


# In[3]:


df = df.set_index('Person')
useravg = df.mean(axis=1).round(decimals=2)

movieavg = df.mean().round(decimals=2)
print(useravg,'\n',movieavg)


# In[4]:


df_tp = df.T
dfnormal = (df_tp - df_tp.min()) / (df_tp.max() - df_tp.min())
dfnormal


# In[5]:


movie_norm = dfnormal.mean(axis=1).round(decimals=5)
user_norm = dfnormal.mean().round(decimals=5)

print(user_norm,'\n',movie_norm)


# In[6]:


df_byMovie = (df - df.min()) / (df.max() - df.min())
df_byMovie


# In[7]:


useravg_byMovie = df_byMovie.mean(axis=1).round(decimals=5)

movieavg_byMovie = df_byMovie.mean().round(decimals=5)
print(useravg_byMovie,'\n',movieavg_byMovie)


# In[8]:


#An advantage of normalizing ratings by user is that if a person always gives very high or low ratings for everything, 
#then their scores won't mean much. Normalizing them would give more weight to smaller scoring differences.

