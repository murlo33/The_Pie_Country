tup = 1, 2, 3, 4, 5  #кортеж

a, b, *ron = tup
print(*ron, sep="x")
print(a, b, sep="_")
print(tup)