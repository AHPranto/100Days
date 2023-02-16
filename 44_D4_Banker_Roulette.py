# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

import random
name_string = input("Give me everybody's names, separated by a comma. ")
names = name_string.split(", ")

num_items = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0,num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]
# person_who_will_pay = random.choice(names)

print(person_who_will_pay + " is going to buy the meal today!")