cost = 14.99
taxperc = 23
tax = taxperc / 100.0
salepr = cost * (1.0 + tax)
print("Sale Price:", salepr)
print("Sale Price: %0.2f" % salepr)