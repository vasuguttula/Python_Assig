# Assignment-1: if condition
# Check if a person is eligible to vote based on their age
# Input: Age of the person
# Check if the person is eligible to vote

voter_age = int(input('Enter Age: '))
if voter_age >= 18:
    print("Voter is Eligible to vote")
else:
    print("Voter is Not Eligible to vote")

# Assignment-2: if else condition
# WAP that checks whether a number is positive or negative

num = int(input("Enter a Number: "))
if num > 0:
    print(f'{num} is Positive Number')
else:
   print(f'{num} is Negative Number')


# Assignment-3: if else condition
# WAP that Checks if a given number is even or odd

num = int(input("Enter a Number: "))
if (num % 2) == 0:
    print(f'{num} is Even Number')
else:
    print(f'{num} is Odd Number')

# Assignment-4: nested if condition
# WAP to find the greatest of 3 numbers

num1 = int(input('Number-1: '))
num2 = int(input('Number-2: '))
num3 = int(input('Number-3: '))
if num1 > num2:
    if num1 > num3:
        print(f'Number {num1} is Grater')
if num2 > num1:
    if num2 > num3:
        print(f'Number {num2} is Grater')
if num3 > num1:
    if num3 > num2:
        print(f'Number {num3} is Grater')

# Assignment-5: nested if else condition
"""

Movie Ticket Pricing
Imagine a movie theater that offers different ticket prices based on the age of the customer and the time of the day. The rules might be as follows:

Regular price: $10
Children under 12 and seniors over 65 get a 50% discount.
Matinee show (before 5 PM) offers a 25% discount to all.
"""
age = int(input("Enter the Coustmer Age: "))
time = int(input("Enter the Time in 24hr Format: "))
if age >=65 or age <=12:
    print(f"Total Price: {10*0.5}$")
else:
    if time <= 17:
        print(f"Total Price: {10*0.75}$")
    else:
        print(f"Total Price: {10}$")
# Assignment-6: nested if else condition
# WAP to find the biggest country among 3 based on the population
country_1 = int(input("Enter population of country_1 "))
country_2 = int(input("Enter population of country_2 "))
country_3 = int(input("Enter population of country_3 "))
if country_1 > country_2:
    if country_1 > country_3:
        print("Country_1 is biggest country")
    else:
        print("Country_3 is biggest country")
else:
    if country_2 > country_3:
        print("Country_2 is biggest country")
    else:
        print("Country_3 is biggest country")