import random

number = random.randint(1,9)

guess=0
count=0

while number != exit and guess != number:
    guess = input("make a guess: ")

    if guess == "exit":
        break

    guess = int(guess)

    count += 1

    if guess < number:
        print ("guess is too low")
    elif guess > number:
        print("guess is too high")
    else:
        print("you got it and it took you only", count, "tries")