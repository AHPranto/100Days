# if height avobe 120cm then you can ride otherwise you cant
# if your age > 12 then pay 5,if age <= 10 then pay 7, else pay 12

print("Welcome to the Roller Coaster")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can Ride the Roller coaster.")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay 5 tk")
    elif age <= 18:
        print("Please pay 7 tk")
    else:
        print("Please pay 12 tk")
else:
    print("Sorry, You Can't Ride")
