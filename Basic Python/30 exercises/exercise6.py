wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
print(wrd[4], wrd[-4], len(wrd))
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
