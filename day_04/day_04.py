import pandas as pd
import re

data = pd.read_csv('input.csv', header=None)

subsets = 0
for a, b in zip(data.iloc[:,0], data.iloc[:,1]):
    a, b = [int(a) for a in re.split('-', str(a))], [int(b) for b in re.split('-', str(b))]
    a, b = list(range(a[0], a[1]+1)), list(range(b[0], b[1]+1))
    if set(a).issubset(b) or set(b).issubset(a):
        subsets += 1

print('Number of assignment pairs that fully contains the other:', subsets)

subsets = 0
for a, b in zip(data.iloc[:,0], data.iloc[:,1]):
    a, b = [int(a) for a in re.split('-', str(a))], [int(b) for b in re.split('-', str(b))]
    a, b = list(range(a[0], a[1]+1)), list(range(b[0], b[1]+1))
    if set(a) & set(b):
        subsets += 1

print('Number of overlapping assignment pairs:', subsets)