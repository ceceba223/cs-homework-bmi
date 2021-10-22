height = float(input("How tall are you (in cm)? "))
weight = float(input("How much do you weigh (in kg)? "))
bmi = round((weight / height / height) * 10000, 1)

if bmi < 18.5:          # <18.5 = underweight
    print("You are underweight! Try to eat more.")
    print(f"Your BMI is {bmi}")
elif bmi <= 24.9:       # 18.5-24.9 = normal weight
    print("Your weight is normal.")
    print(f"Your BMI is {bmi}")
elif bmi <= 29.9:       # 25-29.9 = overweight
    print("You are overweight")
    print(f"Your BMI is {bmi}")

    smoking = input("Do you smoke? (Y/n) ").lower
    if smoking == "y":
        print("You should probably stop smoking to start a healthier life-style.")
    else:
        print("Good! You shouldn't start now.")
else:                   # >30 obese
    #print("Ur big boi!!! JK")
    print("You are obese!")
    print(f"Your BMI is {bmi}")

    smoking = input("Do you smoke? (Y/n) ").lower
    if smoking == "y":
        print("You should probably stop smoking to start a healthier life-style.")
    else:
        print("Good! You shouldn't start now.")
print("LG HG")