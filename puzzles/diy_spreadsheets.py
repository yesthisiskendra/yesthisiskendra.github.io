#!/usr/bin/env python
# coding: utf-8

# In[287]:


def create_spreadsheet(r,c):
    return [(['' for col in range(c)]) for row in range(r)]


# In[288]:


def make_pretty(i,col):
    max_len = get_max_len(spreadsheet,i)
    spaces = int(max_len-len(col))
    return col + (f"{' '*spaces}"  + '|')
                          
def get_max_len(spreadsheet, i):
    return max(len(spreadsheet[col][i]) for col in range(3))

def pretty_print(spreadsheet):
    for row in spreadsheet:
       print("".join([make_pretty(i,c) for i,c in enumerate(row)]))


# In[289]:


spreadsheet = create_spreadsheet(4,3)
spreadsheet[0][0] = 'bob'
spreadsheet[0][1] = '10'
spreadsheet[0][2] = 'foo'
spreadsheet[1][0] = 'alice'
spreadsheet[1][1] = '5'


# In[290]:


pretty_print(spreadsheet)


# In[ ]:




