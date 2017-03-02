primeslist = []

with open('primenumbers.txt') as f:
    line = f.readline()
    while line:
        primeslist.append(int(line))
        line = f.readline()

happylist = []
with open('happynumbers.txt') as f:
    line = f.readline()
    while line:
        happylist.append(int(line))
        line = f.readline()

print(primeslist)
print(happylist)

overlaplist = []

for i in primeslist:
    if i in happylist:
        overlaplist.append(i)

print(overlaplist)