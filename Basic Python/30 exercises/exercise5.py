import numpy as np

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

unique_list =[]

for i in a:
    for j in b:
        if i==j:
            unique_list.append(i)

print(np.unique(unique_list))
