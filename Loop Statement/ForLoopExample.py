#Dictionary Iteration:


print("Dictionary Iteration:")

person = {"name": "John", "age": 20, "designation": "Designer"}

#key based Iteration
for key in person:
    print(f"key: {key}")

#value based Iteration
for value in person.values():
    print(f"value: {value}")

#both key and value based Iteration
for key, value in person.items():
    print(f"key: {key}, value: {value}")


#Set Iteration:

# print("Set Iteration:")

# colors = {"Red", "Green", "Blue"}
# for color in colors:
#     print(f"color: {color}")

#Character Iteration:
# print("Character Iteration:")
# name = "Python"
# print(f"name: {name}")

# for ch in name:
#     print(f"ch: {ch}")

# #Tuple Iteration

# print("Tuple Iteration")

# t = (10, 20, 30, 40, "Python")
# print(t)

# for ele in t:
#     print(f"ele: {ele}")

# List Iteration

# print("List Iteration")

# l = [1, 2, 3, 4, "Python"]
# l.append("5")
# print(l)

# for ele in l:
#     print(f"ele: {ele}")
