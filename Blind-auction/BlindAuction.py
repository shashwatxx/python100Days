from typing_extensions import ParamSpecArgs
from logoart import logo
from clearFunction import clear


bidders = []


def placeBid():
    name = input("What is your name? : ")
    bid = int(input("What's your bud? : ₹"))
    bidders.append({"name": name, "bid": bid})
    runAgain()


def showResult():
    highestBid = 0
    highestBidder = ""
    for i in bidders:
        if highestBid < int(i["bid"]):
            highestBid = int(i["bid"])
            highestBidder = i["name"]
    print(f"The Winner is {highestBidder} with a bid of ₹{highestBid}")


def runAgain():
    action = input(
        "Do yo see any collouge? Press 'Y' for Yes  'N' for No\n").lower()
    if action == 'y':
        clear()
        placeBid()
    else:
        clear()
        showResult()


print(logo)
print("Welcome to the secret auction program")
placeBid()
