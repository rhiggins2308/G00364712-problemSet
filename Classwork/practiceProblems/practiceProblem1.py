# Problems: Python Fundamentals
# Problem 1 - return product of 2 integers

def sumultiply(num1, num2):
    total = num1
    count = 1
    while count < num2:
        total += num1
        count += 1
    return total

num1 = int(input("Enter an Integer value:"))
num2 = int(input("Enter another Integer value:"))

total = sumultiply(num1, num2)

print("The product of your chosen numbers is: ", total)