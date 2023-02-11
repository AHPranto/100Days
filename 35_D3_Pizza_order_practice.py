# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Your final bill is: $bill.
# pepperoni = pizzar upore dey ek dhoroner salader moto gol,gol
size = input("What size do you want?: S, M, L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do You want Extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill += 150
elif size == "M":
    bill += 200
else:
    bill += 250

if add_pepperoni == "Y":
    if size == "S":
        bill += 20
    else:
        bill += 30
    
if extra_cheese == "Y":
    bill +=10

print(f"Your Final bill is {bill} tk")



"""
size = input("What size do you want?: S, M, L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do You want Extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill = 150
    if add_pepperoni == "Y":
        bill += 20
    if extra_cheese == "Y":
        bill += 10
        print(f"Your Final Bill {bill}")
if size == "M":
    bill = 200
    if add_pepperoni == "Y":
        bill += 30
    if extra_cheese == "Y":
        bill += 10
        print(f"Your Final Bill {bill}")
if size == "L":
    bill = 250
    if extra_cheese == "Y":
        bill += 10
        print(f"Your Final Bill {bill}")

        """

