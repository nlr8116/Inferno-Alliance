

values = { i : i**2 for i in range(10)}
print(values)

values = { i : "hello" for i in range(10)}
print(values)

values = { i : i**3 for i in range(20) if i % 2 == 0}
print(values)

names = ["William", "Ashish", "Joseph", "Kim", "Aayusha"]
result = { name : len(name)  for name in names}
print(result)

ages = [33000, 21, 13, 26, 900]
result = {   names[i] : ages[i]      for i in range(len(names))}
print(result)

legal_drinkers = {   names[i] : ages[i]      for i in range(len(names)) if ages[i] >= 21}
print(legal_drinkers)
