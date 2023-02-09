""" Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left. """
# year = 365 days, year = 52 days, year = 12 months
# if you live 60 years

age = input("What is your Current AGE?: ")

age_as_int = int(age)

years_remaining = 60 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} month left"

print(message)