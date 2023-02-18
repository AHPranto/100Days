# https://app.codingrooms.com/management/assignments/364939/overview
# divisible 3 -> Fizz
# divisible 5 -> Buzz
# divisible 3 and 5 -> FizzBuzz
# otherwise printed the number

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)