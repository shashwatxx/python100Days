import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
userchoice = int(
    input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.\n"))
computerChoice = random.randint(0, 2)


def computerchoice(computerChoice):
    if computerChoice == 0:
        print(rock)
    elif computerChoice == 1:
        print(paper)
    elif computerChoice == 2:
        print(scissors)


def getWon(a, b):
    if a == b:
        print("It's a draw")
    elif a == 0 and b == 2:
        print("you Won")
    elif a == 1 and b == 0:
        print("You Won!")
    elif a == 2 and b == 1:
        print("You Won!")
    else:
        print("You Lost!")


if userchoice == 0:
    print(rock)
    computerchoice(computerChoice)
    getWon(userchoice, computerChoice)
elif userchoice == 1:
    print(paper)
    computerchoice(computerChoice)
    getWon(userchoice, computerChoice)
elif userchoice == 2:
    print(scissors)
    computerchoice(computerChoice)
    getWon(userchoice, computerChoice)
else:
    print("Wrong Input!!")
