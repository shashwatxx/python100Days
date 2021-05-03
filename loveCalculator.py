yourName = input("What is your Name\n")
loverName = input("What is your Lover's Name\n")

true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]
num1 = 0
num2 = 0
combinedName = yourName+loverName

for i in true:
    num1 += combinedName.lower().count(i)

for j in love:
    num2 += combinedName.lower().count(j)

percentageString = "%d%d" % (num1, num2)
percentage = int(percentageString)
print(percentage)


if(percentage < 10 or percentage > 90):
    print("Your score is "+percentageString +
          ", you go together like coke and mentos.")

elif(percentage > 40 and percentage < 51):
    print("Your score is "+percentageString+", you are alright together.")

else:
    print("Your score is " + percentageString)
