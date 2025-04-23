#Loop Control Statement

for i in range(2):
    for j in range(2):
        print(f"i: [{i}, {j}]")

# First i Iteration
# i = 0
# j = 0
# j = 1

# 2nd i Iteration
# i = 1
# j = 0
# j = 1

# print("continue")

# limit = int(input("Enter the limit: "))

# for i in range(limit):
#     i += 1
#     # print(f"i: {i}")
#     if i % 2 != 0:
#         continue
#     print(f"Even Number is {i}.")
# else:
#     print("Program End")
#break

# print("break")

# limit = int(input("Enter the patient limit: "))

# for i in range(limit):
#     if i > 10:
#         break
#     print(f"Patient {i}'s problem has resolved.")
# else:
#     print("break Program has completed")

#range()

# print("range()")

# limit = int(input("Enter the limit: "))

# for i in range(limit):
#     print(f"i: {i}")

# print("Hue Bank:")

# correctPassword = "Admin"
# maxAttempt = 3
# password = input("Enter the password: ")
# while password != correctPassword and maxAttempt > 1:
#     maxAttempt-= 1 # maxAttempt = maxAttempt - 1
#     password = input("Enter the password: ")

# if maxAttempt > 0:
#     print("Welcome to Hue Bank")
# else:
#     print("Your account has been locked.")