#!/usr/bin/env python
# coding: utf-8

# # Web Scraping 

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


re = requests.get("https://www.imdb.com/list/ls567236703/")


# In[3]:


sp = BeautifulSoup(re.text, "html.parser")


# In[4]:


res = sp.find_all("div", attrs = {"class" : "lister-item-content"})
res[45].find("h3", attrs = {"class" : "lister-item-header"}).text.strip().replace("\n", "")


# In[5]:


res[58].find("span", attrs = {"class" : "ipl-rating-star__rating"}).text


# In[6]:


res[27].find("span", attrs = {"class" : "genre"}).text.strip().replace("\n", "")


# In[7]:


res[27].find("span", attrs = {"class" : "certificate"}).text.strip().replace("\n", "")


# In[8]:


res[0].find("p", attrs = {"class" : ""}).text.strip().replace("\n", "")


# In[9]:


web = []
for r in res:
    Name = r.find("h3", attrs = {"class" : "lister-item-header"}).text.strip().replace("\n", "")
    Rating = r.find("span", attrs = {"class" : "ipl-rating-star__rating"}).text
    Genre = r.find("span", attrs = {"class" : "genre"}).text.strip().replace("\n", "")
    Cirtificate = r.find("span", attrs = {"class" : "certificate"}).text.strip().replace("\n", "")
    Plot = r.find("p", attrs = {"class" : ""}).text.strip().replace("\n", "")
    web.append((Name, Rating, Genre, Cirtificate, Plot))


# In[10]:


len(web)


# In[20]:


df = pd.DataFrame(web, columns = ["Name", "Rating", "Genre", "Cirtificate", "Plot"])


# In[21]:


df.head(5)


# # Data Cleaning

# In[22]:


new = df["Name"].str.split(".", n = 1, expand = True)
df["list"] = new[0]
df["Name"] = new[1]


# In[23]:


new = df["Name"].str.split("(", n = 1, expand = True)
df["year"] = new[1]
df["Name"] = new[0]


# In[24]:


df = pd.DataFrame(df, columns = ["list", "Name", "year", "Rating", "Genre", "Cirtificate", "Plot"])


# In[25]:


df["year"] = df["year"].str.replace("–", "")


# In[26]:


df["year"] = df["year"].str[0:4]


# In[27]:


df


# In[28]:


df.to_csv("top_60_Indian_WebSeries.csv", index = False, encoding = "utf-8")


# In[ ]:




