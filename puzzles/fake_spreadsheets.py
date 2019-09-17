#!/usr/bin/env python
# coding: utf-8

# In[58]:


import re
def create_spreadsheet(rows,columns):
    spreadsheet = []
    for row in range(rows):
        row = []
        for column in range(columns):
            row.append('_')
        spreadsheet.append(row)
    return(spreadsheet) 

def update_spreadsheet(params):
    spreadsheet = params[0]
    r = params[1]
    c = params[2]
    value = params[3]
    spreadsheet[r][c] = value
    return(spreadsheet)

def get_max_len(spreadsheet, i):
    max_len = 0
    for row in spreadsheet:
        if (i < len(row)) and len(str(row[i])) > max_len:
            max_len = len(str(row[i]))
    return(max_len)

def run_function(cell):
    return('hello!')
    
def pretty_print(spreadsheet):
    for r,row in enumerate(spreadsheet):
        for c,cell in enumerate(row):
            if '=' in str(cell):
                result = run_function(cell)
                print(result, r, c)
                spreadsheet[r][c] = result
    return(spreadsheet)


# In[59]:


spreadsheet = create_spreadsheet(4,3)


# In[60]:


update_spreadsheet([spreadsheet,0,0, 'bob'])
update_spreadsheet([spreadsheet,0,1, 10])
update_spreadsheet([spreadsheet,0,2, 'foo'])
update_spreadsheet([spreadsheet,1,0, 'alice'])
update_spreadsheet([spreadsheet,1,1, 5])
update_spreadsheet([spreadsheet,2,1, 15])
update_spreadsheet([spreadsheet,2,0, '=sum(1:2-3:2)'])


# In[61]:


newsheet = pretty_print(spreadsheet)


# In[62]:


newsheet


# In[ ]:




