import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
userCards = [random.choice(cards), random.choice(cards)]
dealerCards = [random.choice(cards), random.choice(cards)]


def addCardforMe():
    userCards.append(random.choice(cards))


def addCardforDealer():
    dealerCards.append(random.choice(cards))


def getScore(cards):
    score = 0
    for card in cards:
        score += card
    return score


def checkResult():
    userSum = getScore(userCards)
    dealerSum = getScore(dealerCards)
    if userSum > 21:
        return "You Lost!"
    elif dealerSum > 21:
        return "You won,Dealer Lost"
    if userSum > dealerSum and userSum < 21:
        return "You Win!!!"
    elif userSum < dealerSum:
        return "You lose,Dealer Won!"
    else:
        return "It's a Draw!"


def dealerMustCondition():
    dealerScore = getScore(dealerCards)
    if(dealerScore > 17):
        addCardforDealer()


def startGame():
    continue_game = True
    print(f"Your Cards are {userCards}")
    print(f"Current score :{getScore(userCards)}")
    print(f"One of Dealer's Card is {dealerCards[1]}")
    while continue_game:
        action = input("Type'y' to get another card,type 'n' to pass")
        dealerMustCondition()
        if(action == 'y'):
            addCardforMe()
            print(f"Your Cards are {userCards}")
            print(f"Current score :{getScore(userCards)}")
            print(f"One of Dealer's Card is {dealerCards[1]}")
        elif(action == "n"):
            print(f"Your Cards are {userCards}")
            print(f"Current score :{getScore(userCards)}")
            print(f"One of Dealer's Card is {dealerCards[1]}")
            print(
                f"Dealer's final hamds are {dealerCards}.His score- {getScore(dealerCards)}")
            print(checkResult())
            continue_game = False


startGame()
