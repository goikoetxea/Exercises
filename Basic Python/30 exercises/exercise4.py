number1 = int(input("Please choose a number to divide: "))

listRange = list(range(1,number1+1))

divisorList = []

for number2 in listRange:
    if number1 % number2 == 0:
        divisorList.append(number2)

print(divisorList)
