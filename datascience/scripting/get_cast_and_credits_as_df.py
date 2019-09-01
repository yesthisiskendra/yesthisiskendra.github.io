#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import matplotlib.pyplot as plt
import statistics
movies = pd.read_csv("clean_movies_usa.csv", encoding="ISO-8859-1")


# In[2]:


avg_actors = pd.DataFrame(movies.groupby(["star", "year"])["score"].mean())
avg_actors_scores = pd.DataFrame()
actors = list(movies['star'].unique())
for actor in actors:
    d = avg_actors.groupby('star').get_group(actor)
    d.reset_index(inplace=True)
    past_scores = []
    for row in range(len(d)):
        past_scores.append(d.iloc[row]['score'])
        actor_df = pd.DataFrame(
            {'star': actor, 'year': d.iloc[row]['year'], 'star_mean': statistics.mean(past_scores)}, index=[0])
        avg_actors_scores = pd.concat([avg_actors_scores, actor_df])


# In[3]:


avg_directors = pd.DataFrame(movies.groupby(
    ["director", "year"])["score"].mean())
avg_directors_scores = pd.DataFrame()
directors = list(movies['director'].unique())
for director in directors:
    d = avg_directors.groupby('director').get_group(director)
    d.reset_index(inplace=True)
    past_scores = []
    for row in range(len(d)):
        past_scores.append(d.iloc[row]['score'])
        director_df = pd.DataFrame(
            {'director': director, 'year': d.iloc[row]['year'], 'director_mean': statistics.mean(past_scores)}, index=[0])
        avg_directors_scores = pd.concat([avg_directors_scores, director_df])


# In[4]:


avg_writers = pd.DataFrame(movies.groupby(["writer", "year"])["score"].mean())
avg_writers_scores = pd.DataFrame()
writers = list(movies['writer'].unique())
for writer in writers:
    d = avg_writers.groupby('writer').get_group(writer)
    d.reset_index(inplace=True)
    past_scores = []
    for row in range(len(d)):
        past_scores.append(d.iloc[row]['score'])
        writer_df = pd.DataFrame(
            {'writer': writer, 'year': d.iloc[row]['year'], 'writer_mean': statistics.mean(past_scores)}, index=[0])
        avg_writers_scores = pd.concat([avg_writers_scores, writer_df])


# In[5]:


s1 = pd.merge(movies, avg_writers_scores, how='left', on=['writer', 'year'])
s2 = pd.merge(s1, avg_directors_scores, how='left', on=['director', 'year'])
s3 = pd.merge(s2, avg_actors_scores, how='left', on=['star', 'year'])


# In[7]:


movies_with_mean = s3


# In[8]:


movies_with_mean


# In[ ]:
