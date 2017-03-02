#Write a program whichaccepts a sequence of comma-separated numbers from
#console and generate a list and a tuple which contains every number.

numbers = input("Enter list of numbers:")

l = numbers.split(",")
print(l)
print(tuple(l))
