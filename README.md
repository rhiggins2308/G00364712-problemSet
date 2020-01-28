# G00364712 Problem Set 2018

## H.Dip. Data Analytics - Programming & Scripting - Problem Set for Grading
Please Note: New repository for Problem Set, due to issues with syncing local folder with original repository.
For all previous commit details, please see repository https://github.com/rhiggins2308/G00364712

This new repository has been cleaned of all other practice problems and script files renamed to correspond with the relevant task as per GMIT moodle course page.

Contains files written in Python

### To run files:
1. Download & Install Anaconda
2. Download & Install Visual Studio Code
3. Navigate to local folder containing scripts (if downloaded to local machine)
4. type the command "python" followed by a space, then the name of the file you wish to execute (including file extension .py)

The contents of the repository are as follows:

### exercise1.py
  contains a function defined to calculate the nth Fibonacci number, based on an integer value passed to it.
  Integer value will be made up of the numbers corresponding to the sum of the alphabetic positions of the first and last letters of a
  first name.
  No user input is required.
  Program simply outputs a Fibonacci number based on pre-defined values

### exercise2.py
  A progression from exercise1.py
  This time a pre-defined string is used and code identifies the first and last letters of the string, printing them to screen
  Identifies the ASCII representation of these letters using Python's ord() function and prints these to screen
  These ASCII values are summed and passed to the same fib() function to calculate the relevant Fibonacci number, which is printed to
  screen
  No user input is required.

### exercise3.py
  Demonstrates the Collatz conjecture, that no matter what positive integer we start with, we will always reduce it to 1, by using two
  operations based on opposite logic tests.
  i.e. if the number is even, we divide it by 2. If the number is odd, we triple it and add 1. We then repeat the process with the result,
  until we finish with a value of 1
  No user input is required.
  User inputs any positive variable to begin the calculation

### exercise4.py
  From projecteuler.net
  Problem number 5, calculate the LCM of all natural numbers to 20, inclusive

### exercise5.py
  Uses Fishers iris data set
  code opens, reads and prints the contents of the file
  formatted in a table with decimal alignment
  
### exercise6.py
  Calculate the factorial of a number using a function
  Factorial is a mathematical term simply meaning we start at the given number and multiply it by every natural number less than itself.

