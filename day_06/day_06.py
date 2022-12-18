with open('input.csv') as file:
    data = file.read()

for i in range(len(data)):
    if len(set(data[i:i+4])) == 4:
        print(i+4, "characters need to pe processed before first start-of-packet marker.")
        break

for i in range(len(data)):
    if len(set(data[i:i+14])) == 14:
        print(i+14, "characters need to pe processed before first start-of-message marker.")
        break