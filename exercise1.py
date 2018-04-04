# G00364712 Robert Higgins - Exercise 1
# A program that displays the nth Fibonacci number via a function, which is called using input of users first.
# adapted from lecture video by Ian McLoughlin

def fib(n):
  #This function returns the nth Fibonacci number.
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
# First letter of first name is R, corresponding to the number 18
# Last letter of first name is T, corresponding to the number 20

first = 18
last = 20

sum = first + last
ans = fib(sum)
print("Fibonacci number", sum, "is", ans)
# Fibonacci number 38 is 39088169