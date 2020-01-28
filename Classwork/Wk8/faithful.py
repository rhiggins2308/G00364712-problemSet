# Robert Higgins, 2018-04-29
# Old Faithful Analysis

# Calculate mean of each column
import numpy
data = numpy.genfromtxt('oldfaithful.csv', delimiter=',')

firstcol = data[:,0]
secondcol = data[:,1]

meanfirstcol = numpy.mean(firstcol)
meansecondcol = numpy.mean(secondcol)

print("Mean Eruption Time:", meanfirstcol)
print("Mean Time Between Eruptions:", meansecondcol)

