#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

tn_df = pd.read_csv('0909_TN_all.csv')

def return_just_num(num):
    num = num.split('$')[1]
    num = num.replace(',','')
    return(num)
    
tn_df['ww_bo'] = tn_df.apply(lambda x: return_just_num(x['WorldwideBoxOffice']),axis=1)
tn_df['int_bo'] = tn_df.apply(lambda x: return_just_num(x['InternationalBoxOffice']),axis=1)
tn_df['dom_bo'] = tn_df.apply(lambda x: return_just_num(x['DomesticBoxOffice']),axis=1)
tn_df['prod_budget'] = tn_df.apply(lambda x: return_just_num(x['ProductionBudget']),axis=1)    


# In[2]:


##################################
## GET PRODUCTION STAFF
##################################
all_movies_production = []
for index, row in tn_df.iterrows():
    all_production = []
    for person in eval(row['production']):
        new_row = {}
        new_row.update({ 'title': row['Title'] })
        new_row.update({ 'role': list(person.keys())[0] })
        new_row.update({ 'person': list(person.values())[0] })
        new_row.update({ 'dom_percent_profit': (float(row['dom_bo'])/(float(row['dom_bo']) - float(row['prod_budget'])))*100 })
        new_row.update({ 'int_percent_profit': (float(row['int_bo'])/(float(row['int_bo']) - float(row['prod_budget'])))*100 })      
        new_row.update({ 'genre': row['Genre'] })
        all_production.append(new_row)
    all_movies_production += all_production


# In[3]:


##################################
## GET LEADS
##################################
all_movies_leads = []
for index, row in tn_df.iterrows():
    new_row = {}
    all_leads = []
    for person in eval(row['leads']):
        new_row = {}
        new_row.update({ 'title': row['Title'] })
        new_row.update({ 'role': 'lead' })
        new_row.update({ 'person': person })
        new_row.update({ 'dom_percent_profit': (float(row['dom_bo'])/(float(row['dom_bo']) - float(row['prod_budget'])))*100 })
        new_row.update({ 'int_percent_profit': (float(row['int_bo'])/(float(row['int_bo']) - float(row['prod_budget'])))*100 })      
        new_row.update({ 'genre': row['Genre'] })
        all_leads.append(new_row)
    all_movies_leads += all_leads


# In[4]:


##################################
## GET SUPPORTING CAST
##################################
all_movies_supporting = []
for index, row in tn_df.iterrows():
    new_row = {}
    all_supporting = []
    for person in eval(row['supporting']):
        new_row = {}
        new_row.update({ 'title': row['Title'] })
        new_row.update({ 'role': 'supporting' })
        new_row.update({ 'person': person })
        new_row.update({ 'dom_percent_profit': (float(row['dom_bo'])/(float(row['dom_bo']) - float(row['prod_budget'])))*100 })
        new_row.update({ 'int_percent_profit': (float(row['int_bo'])/(float(row['int_bo']) - float(row['prod_budget'])))*100 })      
        new_row.update({ 'genre': row['Genre'] })
        all_supporting.append(new_row)
    all_movies_supporting += all_supporting


# In[5]:


print(len(all_movies_production))
print(len(all_movies_leads))
print(len(all_movies_supporting))


# In[6]:


all_movies = []
all_movies += all_movies_production
all_movies += all_movies_leads
all_movies += all_movies_supporting
all_movies_df = pd.DataFrame(all_movies)


# In[42]:



all_movies_df = all_movies_df.drop_duplicates()
all_movies_df['person_count_overall'] = all_movies_df.groupby('person')['person'].transform('count')
all_movies_df['person_role_count'] = all_movies_df.groupby(['person', 'role'])['person'].transform('count')
all_movies_df['person_role_count'] = all_movies_df.groupby(['person', 'role'])['person'].transform('count')


# In[43]:


## TESTING
len(all_movies_df[(all_movies_df['role'] == 'Composer') & (all_movies_df['person_count_overall'] > 2)])


# In[44]:


df = all_movies_df
df = df.drop_duplicates()


# In[45]:


print(len(all_movies_df))
print(len(df))


# In[46]:


df[df['person'] == 'Chris Columbus']


# In[47]:


df.sort_values(by='person_count_overall', ascending=False)[:100]


# In[48]:


all_movies_df.to_csv('0911_TN_longform_v2.csv')


# In[49]:


randy = all_movies_df[all_movies_df['person'] == 'Randy Thom']


# In[50]:


randy


# In[51]:


len(randy)


# In[ ]:


# randy.groupby('')

