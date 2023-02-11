# if height avobe 120cm then you can ride otherwise you cant
# if your age > 12 then pay 5,if age <= 10 then pay 7, else pay 12
# Whants photo? bill +3
# 45-55 ages people are free ride
print("Welcome to the Roller Coaster")

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can Ride the Roller coaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay 5 tk")
    elif age <= 18:
        bill = 7
        print("Please pay 7 tk")
    elif age >=45 and age<=55:
        print("Have a Free ride on us!")
    else:
        bill = 12
        print("Please pay 12 tk")
    wants_photo = input("Do You Wants Photo? Y or N: ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your Final bill: {bill} Tk")
else:
    print("Sorry, You Can't Ride")
