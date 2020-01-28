# G00364712 Robert Higgins - Exercise 5
# Fishers Iris Data Set
# code opens, reads and prints the contents of the file
# formatted in a table with decimal alignment

with open("data/iris.csv") as iris:
    for line in iris:
       print('{} {} {} {}'.format(line.split(',')[0].ljust(4), line.split(',')[1].ljust(4), line.split(',')[2].ljust(4), line.split(',')[3].ljust(4)))