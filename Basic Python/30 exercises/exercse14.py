x = [1,2,3,4, 1, 2, 5]
y = []

def list_without_duplicates(x):
    for i in x:
        if i not in y:
            y.append(i)
    return y

list_without_duplicates(x)
print(y)


def list_without_duplicates2(x):
    return list(set(x))

a = [1,2,3,4, 1, 2, 5]
print(list_without_duplicates2(a))