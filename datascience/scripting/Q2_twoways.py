import pandas as pd
import numpy as np

# reading the csv
data = pd.read_csv('EUR.pop.rev.csv')

# creating a backup to play with
df = data

# QUESTION 1
# replace missing data with 0
df = df.fillna(0)
print('QUESTION #1')
print(df)

# QUESTION 2:
# print countries with populations > 1 mil
large_countries = []
for index, row in df[2:19].iterrows():
    if int(row[-1]) > 1000000:
        large_countries.append(row[0])
print('QUESTION #2')
print(large_countries)

# QUESTION 3
# getting the mean of UK
# getting the 18th row (for United Kingdom)
# taking only the year columns
uk = df.iloc[18, 1:8]

print('QUESTION #3')
print(uk.mean())


# THE CLEAN WAY
df = data

# renaming columns
new_col_names = ['country', '1989', '1990',
                 '1991', '1992', '1993', '1994', '1995']
df.columns = new_col_names

# removing NaNs (replacing with 0)
df = df.fillna(0)

# QUESTION 1
# removing rows that are all 0s
df = df.loc[(df != 0).any(1)]
print("V2 QUESTION #1")
print(df)

# dropping the first two and last rows
df = df.drop(df.index[[0, 1]])
df = df.drop(df.index[-1])

# changing the first column to an index
df.set_index('country', inplace=True)

# QUESTION 2


def get_large_countries(x, y):
    if int(y) > 1000000:
        return(x)


print("V2 QUESTION #2")
result = [get_large_countries(x, y) for x, y in zip(df.index, df['1995'])]
print(result)


# QUESTION 3
print("V2 QUESTION #3")
print(df.loc['United Kingdom'].mean())
