import pandas as pd
import string

data = pd.read_csv('input.csv', header=None, names=['full'])
priority = [0] + [*string.ascii_lowercase] + [*string.ascii_uppercase]

data['left'] = [i[:len(i)//2] for i in data.full]
data['right'] = [i[len(i)//2:] for i in data.full]

match = []
for i, rucksack in enumerate(data.left):
    for item in rucksack:
        if item in data.right[i]:
            match.append(item)
            break

data['match'] = match
data['prio'] = [priority.index(i) for i in data.match]
print('Sum of priorities:', data['prio'].sum())

match = []   
for r in range(0, len(data.full), 3):
    for item in data.full[r]:
        if item in data.full[r+1] and item in data.full[r+2]:
            match.append(item)
            break

print('Sum of priorities of badges:', sum([priority.index(i) for i in match]))