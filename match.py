status = "Start"

match status.lower():
    case "start" | "working":
        print("In-Progress")
    case "stop" | "end":
        print("Stopping")
    case _:
        print("Invalid Status")

# l = (1, 2)

# match l:
#     case (1, 1):
#         print("1")
#     case (1, 2):
#         print("2")
#     case (1, 3):
#         print("3")
#     case _:
#         print("Default Case")

# statusCode = int(input("Enter the http status code: "))

# match statusCode:
#     case 200:
#         print("okay")
#     case 201:
#         print("Created")
#     case 404:
#         print("Page not found")
#     case _:
#         print("Invalid http status code")

# statusCode = input("Enter the http status code: ")

# match statusCode:
#     case "200":
#         print("okay")
#     case "201":
#         print("Created")
#     case "404":
#         print("Page not found")
#     case _:
#         print("Invalid http status code")

# num = int(input("Enter the number: "))

# match num:
#     case _ if num < 10:
#         print("Number is less than 10")
#     case _ if num > 10 & num < 20:
#         print("Number between 11 and 19")
#     case _:
#         print("Invalid Number.")
