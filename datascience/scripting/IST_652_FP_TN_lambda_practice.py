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

all_movies = []
for index, row in tn_df.iterrows():
    new_row = {}
    all_production = []
#     print(row['Title'])
    for person in eval(row['production']):
        new_row = {}
        new_row.update({ 'title': row['Title'] })
        new_row.update({ 'role': list(person.keys())[0] })
        new_row.update({ 'person': list(person.values())[0] })
        new_row.update({ 'dom_percent_profit': (float(row['dom_bo'])/(float(row['dom_bo']) - float(row['prod_budget'])))*100 })
        new_row.update({ 'int_percent_profit': (float(row['int_bo'])/(float(row['int_bo']) - float(row['prod_budget'])))*100 })      
        new_row.update({ 'genre': row['Genre'] })
        print(new_row)
        all_production.append(new_row)
    all_movies += all_production