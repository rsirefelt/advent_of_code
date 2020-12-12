list2 = list()
with open('dag3_input.txt') as f:
    for line in f:
        list2.append(line.rstrip().replace(".", "0").replace("#", "1"))

# Uppgift 1: 0 är prickar, 1 är träd
total = 0
n = 0
for line in list2:
    res = [line] * 40
    a = ''.join(res)
    str1 = a.replace(',', '').replace(' ', '')
    if str1[n] == '1':
        total += 1
        n += 3
    else:
        n += 3
print("Antal granar jag kört in i:", total)

# Uppgift 2

# Rad 1
total1 = 0
n = 0
for line in list2:
    res = [line] * 40
    a = ''.join(res)
    str1 = a.replace(',', '').replace(' ', '')
    if str1[n] == '1':
        total1 += 1
        n += 1
    else:
        n += 1

# Rad 3 (Rad 2 = Uppgift 1)

total3 = 0
n = 0
for line in list2:
    res = [line] * 60
    a = ''.join(res)
    str1 = a.replace(',', '').replace(' ', '')
    if str1[n] == '1':
        total3 += 1
        n += 5
    else:
        n += 5

# Rad 4

total4 = 0
n = 0
for line in list2:
    res = [line] * 80
    a = ''.join(res)
    str1 = a.replace(',', '').replace(' ', '')
    if str1[n] == '1':
        total4 += 1
        n += 7
    else:
        n += 7

# Rad 5

total5 = 0
n = 0

list3 = list2[::2]

for line in list3:
    res = [line] * 40
    a = ''.join(res)
    str1 = a.replace(',', '').replace(' ', '')
    if str1[n] == '1':
        total5 += 1
        n += 1
    else:
        n += 1

print("Massor av träd:", total * total1 * total3 * total4 * total5)
