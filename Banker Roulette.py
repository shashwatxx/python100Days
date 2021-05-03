import random


nameString = input("Give me everybody's names,sperated by a comma.\n")
names = nameString.split(',')

selectedindex = random.randint(0, len(names)-1)
print(names[selectedindex]+"is going to buy meal today!")
