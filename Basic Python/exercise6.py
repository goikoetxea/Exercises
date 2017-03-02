#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.

import math

C = 50
H = 30
D = input("Please enter the value of D: " )

i = [x for x in D.split(",")]

Qs = []

for d in i:
    Q = str(round(math.sqrt (2 * C * float(d) / H)))
    Qs.append(Q)

print (",".join(Qs))