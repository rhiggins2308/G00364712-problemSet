# G00364712 Robert Higgins - Exercise 6
# function to calculate the factorial of a given number
# tested with three assigned values, 5, 7 and 10

def factorial(number):
    factProd = 1
    while number > 1:
        factProd *= number
        number -= 1
    return factProd

num1 = 5
num2 = 7
num3 = 10

print(f'The value of {num1} factorial is: {factorial(num1)}')
print(f'The value of {num2} factorial is: {factorial(num2)}')
print(f'The value of {num3} factorial is: {factorial(num3)}')