# Robert Higgins 07/02/18
# Programming & Scripting - Week 3: While Loops

i = 1   # Initialises a variable i with a value of 1
while i <= 10: # Do the following indented code, as long as i has a value of 10 or less
    print(i) # Print the current value for i
    i += 1 # add 1 to the current value of i, and assign the resulting value to i

print("The final value for i is:", i) # not indented, so not part of the while loop. Only runs once, after while loop is finished

# Version of while loop with DECREASING integer values
i = 10   # Initialises a variable i with a value of 1
while i >= 1: # Do the following indented code, as long as i has a value of 10 or less
    print(i) # Print the current value for i
    i -= 1 # add 1 to the current value of i, and assign the resulting value to i
    
print("The final value for i is:", i) # not indented, so not part of the while loop. Only runs once, after while loop is finished