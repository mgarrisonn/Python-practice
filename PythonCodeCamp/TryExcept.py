
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input")

try:
    value = 10/0
except ZeroDivisionError as err:
    print(err)
