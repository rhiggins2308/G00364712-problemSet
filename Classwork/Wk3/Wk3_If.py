# Robert Higgins 07/02/18
# Programming & Scripting - Week 3: While Loops
# Adapted from https://docs.python.org/3/tutorial/controlflow.html#if-statements

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

print("The final value of x is:", x)