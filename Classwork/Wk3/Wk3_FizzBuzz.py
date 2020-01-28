# Robert Higgins 07/02/18
# Programming & Scripting - Week 3: FizzBuzz
# https://en.wikipedia.org/wiki/Fizz_buzz
i = 1

while i <= 100:
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    i += 1