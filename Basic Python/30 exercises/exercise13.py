number= int(input("How many Fibonnaci numbers do you want?"))
a=[1,1]

def fibo():
    a.append (a[len(a)-1]+a[len(a)-2])
    return

while len(a) < number:
    fibo()
    print (a)