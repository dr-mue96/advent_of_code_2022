import pandas as pd
input = pd.read_csv('input.csv', delimiter=' ', skip_blank_lines=False, header=None).squeeze()
calories_per_elf = []
calories = 0
for i in input:
    if i > 0:
        calories += i
    else:
        calories_per_elf.append(calories)
        calories = 0
print('Elf with most calories:', max(calories_per_elf))
print('Sum of the three elves with most calorires:', sum(sorted(calories_per_elf, reverse=True)[:3]))