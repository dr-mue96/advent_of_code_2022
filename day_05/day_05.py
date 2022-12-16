import pandas as pd
import numpy as np
import re
import copy

c = [['F', 'C', 'P', 'G', 'Q', 'R'],
     ['W', 'T', 'C', 'P'],
     ['B', 'H', 'P', 'M', 'C'],
     ['L', 'T', 'Q', 'S', 'M', 'P', 'R'],
     ['P', 'H', 'J', 'Z', 'V', 'G', 'N'],
     ['D', 'P', 'J'],
     ['L', 'G', 'P', 'Z', 'F', 'J', 'T', 'R'],
     ['N', 'L', 'H', 'C', 'F', 'P', 'T', 'J'],
     ['G', 'V', 'Z', 'Q', 'H', 'T', 'C', 'W']]

data = pd.read_csv('input.csv', header=None)
data = pd.DataFrame([re.findall("\d+", i) for i in data.squeeze()], columns=['move', 'from', 'to']).astype(int)

containers = copy.deepcopy(c)
def move(m, f, t):
    for i in range(m):
        containers[t-1].append(containers[f-1][-1])
        del containers[f-1][-1]

for m in data.index:
    move(*data.iloc[m,:])
print('Crates on top of the stacks on CrateMover9000:', *[i[-1] for i  in containers])

containers = copy.deepcopy(c)
def move(m, f, t):
    containers[t-1] += containers[f-1][-m:]
    del containers[f-1][-m:]

for m in data.index:
    move(*data.iloc[m,:])
print('Crates on top of the stacks on CrateMover9001:', *[i[-1] for i  in containers])