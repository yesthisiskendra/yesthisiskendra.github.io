import pandas as pd
donors = pd.read_csv('donors_data.csv')
# FIRST ATTEMPT
wealth0 = donors[donors.WEALTH == 0]
wealth1 = donors[donors.WEALTH == 1]
wealth2 = donors[donors.WEALTH == 2]
wealth3 = donors[donors.WEALTH == 3]
wealth4 = donors[donors.WEALTH == 4]
wealth5 = donors[donors.WEALTH == 5]
wealth6 = donors[donors.WEALTH == 6]
wealth7 = donors[donors.WEALTH == 7]
wealth8 = donors[donors.WEALTH == 8]
wealth9 = donors[donors.WEALTH == 9]

print("group 0", sum(wealth0.HV) / len(wealth0))
print("group 1", sum(wealth1.HV) / len(wealth1))
print("group 2", sum(wealth2.HV) / len(wealth2))
print("group 3", sum(wealth3.HV) / len(wealth3))
print("group 4", sum(wealth4.HV) / len(wealth4))
print("group 5", sum(wealth5.HV) / len(wealth5))
print("group 6", sum(wealth6.HV) / len(wealth6))
print("group 7", sum(wealth7.HV) / len(wealth7))
print("group 8", sum(wealth8.HV) / len(wealth8))
print("group 9", sum(wealth9.HV) / len(wealth9))

for group in donors.WEALTH:
    print(group)

# SECOND ATTEMPT LOL!!
# AND NOW, IN ONE LINE!!!
# The sums
print(donors.groupby("WEALTH").HV.sum())
# The averages
print(print(donors.groupby("WEALTH").HV.sum()/donors.groupby("WEALTH").HV.count()))
# By both wealth and number of children
print(donors.groupby(["WEALTH", 'NUMCHLD']).HV.sum())
# By both wealth and gender
print(donors.groupby(["WEALTH", 'gender dummy']).HV.sum())
