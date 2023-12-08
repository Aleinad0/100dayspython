# height = float (input())
# weight = int (input())

# bmi = weight/(height * height)

# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is{bmi}, you are clinically obese.")

## Leap year

year = int(input())

if year%4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year')
        else:
            print('Not leap year')
    else:
        print('Leap year')
else:
    print('Not leap year')    