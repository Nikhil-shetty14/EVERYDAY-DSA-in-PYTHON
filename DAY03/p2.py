"""Sets operations practice."""

a = {1,2,3}
b = {4,5,6}

print(a|b)

print(a.union(b))

print(a - b) #elements of a only

a = {1,2}
b = {1,2,3}

print(a.issubset(b))

common = a & b
print(common)

