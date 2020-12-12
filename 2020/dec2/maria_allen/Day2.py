list2 = list()
with open('dag2_input.txt') as f:
    for line in f:
        list2.append(line.rstrip().replace(
            "-", " ").replace(":", " ").replace("  ", " ").split(" "))

# Uppgift 1


def split(word):
    return [char for char in word]  # för att dela upp sista indexet


total = 0
for line in list2:
    a = line[2]            # bokstaven vi letar efter
    b = int(line[0])       # lägsta siffran
    c = int(line[1])       # högsta siffran
    d = split(line[3])     # d blir liten lista av sista bokstavskombinationen
    e = d.count(a)
    if e >= b and e <= c:
        total += 1

print("Heja alla tomtenissar som ska med, vilket är:", total)


# Uppgift 2

total1 = 0
for line in list2:
    a = line[2]                 # bokstaven vi lear efter
    b = int(line[0])            # berättar index-plats + 1 för 1 av siffrorna
    c = int(line[1])            # berättar indexplats + 1 för nästa siffra
    d = split(line[3])          # d blir lista av sista bokstavskombinationen

    if a is d[b - 1] and a is not d[c - 1]:
        total1 += 1
    if a is not d[b - 1] and a is d[c - 1]:
        total1 += 1

print("Denna gången kommer bara några nissar med:", total1)
