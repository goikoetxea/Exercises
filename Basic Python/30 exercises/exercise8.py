import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return ("It´s a tie")
    elif u1 == 'paper':
        if u2 == "rock":
            return ("Paper wins!")
        else:
            return ("scissor wins!")
    elif u1 == "rock":
        if u2 == "paper":
            return ("paper wins!")
        else:
            return("rock wins")
    elif u1 == "scissor":
        if u2 == "paper":
            return ("scissor wins!")
        else:
            return ("rock wind!")
    else:
        return("Invalid input")
        sys.exit()

print(compare(user1_answer, user2_answer))

