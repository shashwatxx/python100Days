height = float(input("Enter your height in m\n"))
weight = float(input("Enter your weight in kg\n"))

bmi = round((weight/height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}.You are UnderWeight")
elif bmi < 25:
    print(f"Your BMI is {bmi}.You have a Normal Weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}.You are OverWeight")
elif bmi < 35:
    print(f"Your BMI is {bmi}.You are Obese")
else:
    print(f"Your BMI is {bmi}.You are Clinicaly obese")
