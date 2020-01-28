# Problems: Python Fundamentals
# Problem 2 - check if a string is a palindrome

def isPalindrome(userWord):
    fromLeft = 0
    fromRight = len(userWord) - 1
    isPalindrome = True

    while fromLeft != fromRight:
        if userWord[fromLeft] == userWord[fromRight]:
            fromLeft += 1
            fromRight -= 1
        else:
            isPalindrome = False
            return False
            exit
    
    return isPalindrome

userWord = input("Please enter a word:")
value = isPalindrome(userWord)
if value == True:
    print("The word \"", userWord, "\" is a Palindrome.")
else:
    print("The word \"", userWord, "\" is not a Palindrome.")

