#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import csv
import pandas as pd
from urllib.parse import quote

headers = {'Accept-Language': 'en-US'}
payload = "{}" 


# In[3]:


big_movies = pd.read_csv("movies_from_actors.csv", encoding = "ISO-8859-1",lineterminator='\n')
movies_usa = pd.read_csv("working_movies_usa.csv", encoding = "ISO-8859-1")


# In[4]:


big_movies_clean = pd.DataFrame({ 
    "id": big_movies['id'],
    "imdb_id": big_movies['imdb_id'],
    "name": big_movies['title'], 
    "budget": big_movies['budget'],
    "revenue": big_movies['revenue'],
    "runtime": big_movies['runtime'],
    "score": big_movies['vote_average'],
    "vote_count": big_movies['vote_count'],
    "released": big_movies['release_date'],
    "tagline": big_movies['tagline']
})


# In[9]:


def get_all_from_list(list_of_things, num, key_to_get):
    if list_of_things == '[]':
        return 'na'
    else:
        try:
            return eval(list_of_things)[num][key_to_get]
        except:
            return eval(list_of_things)[0][key_to_get]

# the slash at the end of the line is so we can split it into two lines
# PRODUCTION COMPANIES
big_movies_clean['production_company_1'] = big_movies.apply     (lambda x: get_all_from_list(x['production_companies'], 0, 'name'),axis=1)
big_movies_clean['production_company_2'] = big_movies.apply     (lambda x: get_all_from_list(x['production_companies'], 1, 'name'),axis=1)
big_movies_clean['production_company_3'] = big_movies.apply     (lambda x: get_all_from_list(x['production_companies'], 2, 'name'),axis=1)

# GENRES
big_movies_clean['genre_1'] = big_movies.apply     (lambda x: get_all_from_list(x['genres'], 0, 'name'),axis=1)
big_movies_clean['genre_2'] = big_movies.apply     (lambda x: get_all_from_list(x['genres'], 1, 'name'),axis=1)
big_movies_clean['genre_3'] = big_movies.apply     (lambda x: get_all_from_list(x['genres'], 2, 'name'),axis=1)


# In[11]:


big_movies_clean.to_csv('big_movies_clean_v2.csv')


# In[ ]:




