number = int(input("Please enter a number: "))
check = int(input("Please enter a number to divide by: "))

if number % 4 == 0:
        print ("it is a multiple of 4")
elif number % 2 == 0:
        print ("it is an even number")
else:
        print ("it is an odd number")

if number % check ==0:
    print (number, " divides evenly by ", check)
else:
    print (number, "does not divide evenly by ", check)

