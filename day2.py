## LIFE IN WEEKS 

# age = input('How old are you? ')

# years_left = 90 - int(age)
# weeks = years_left *52

# # print("You have "+ str(weeks) +" left")
# print(f"You have {weeks} left")

# TIP CALCULATOR

print('Welcome to the tip calculator.')
bill = float(input("What was the total bill $"))
tip = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

tip_as_percentage= tip/100
total_tip = bill *tip_as_percentage
bill_with_tip = total_tip + bill
bill_per_person = bill_with_tip / people
pay_per_person = round(bill_per_person,2)
final_amount = "{:.2f}".format(pay_per_person)
print(f'Each person should pay ${final_amount}')

