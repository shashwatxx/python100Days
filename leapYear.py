
year = int(input("enter the year\n"))


# if(year % 4 == 0):
#     if(year % 100 != 0):
#         if(year % 400 != 0):
#             print("It's a Leap Year!")
#         else:
#             print("It's not a Leap Year")
#     else:
#         print("It's not a Leap Year")
# else:
#     print("Its not a Leap Year")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
