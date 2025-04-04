#combining Sets
a = {1, 2, 3}
b = {3, 4, 5}

print(f"a = {a}")
print(f"{b=}")

#Union - Everything in a and everything in b 
#a OR b
#notationally: a | b
print("a | b = ", a | b)

#intersection - Items that are in a and are in b 
#logically a AND b
#notationally: a & b
print("a & b = ", a&b)

#Difference - a - b includes items in a that are not in b 
print("a - b = ", a - b) 
