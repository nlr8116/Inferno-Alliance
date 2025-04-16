# Combining Sets

a = {1, 2, 3}
b = {3, 4, 5}

print("a = ", a)
print(f"{b=}")

# Union - everything in a along with everything in b
# Logically: a OR b
# Notationally: a | b
print("a | b = ", a | b)

# Intersection - items that are in a and are in b 
# Logically: a AND b
# Notationally: a & b
print("a & b = ", a & b)

# Difference - (a - b) includes items in a that are not in b
print("a - b = ", a - b)