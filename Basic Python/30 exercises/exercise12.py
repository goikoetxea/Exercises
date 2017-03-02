
a= [5, 10, 15, 20, 25]

def list_start_end(list_a):
    return (list_a[0], list_a[len(list_a)-1])
n=6
print(list_start_end(a))
for i in range(2, n):
    print(i)