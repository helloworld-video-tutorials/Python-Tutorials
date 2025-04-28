def newLine():
    print("\n")

# def decorate(dec, count):
#     print(dec*count)

def decorate(dec = "=", count = 30):
    print(dec*count)

def generateInvoice(*args, **kArgs):
    #*args - Position Args - ({}, {}, {}, {}, {})
    #*kArgs - Dictionary - {}
    
    # print(args)
    # print(kArgs)

    #decorate("=", 30)
    decorate()
    print("Invoice Generator:")
    decorate()

    print("List of Items:")
    decorate("-")
    totalCost = 0
    
    #* args - Tuple ({}, {}, {}, {}, {})
    for d in args:
        #d - Dictionary
        for key, value in d.items():
            print(f"{key}: {value}")
            if key.lower() == "cost":
                totalCost+=value
        newLine()

    print("Customer Details:")
    decorate("-")
    for key, value in kArgs.items():
        print(f"{key}: {value}")

    newLine()
    print(f"Total Cost: {totalCost}")
    # decorate("-", 30)
    decorate(count = 40, dec = "*")

generateInvoice(
    {"SNo": "Item-123", "Name": "Pencil", "Cost": 5},
    {"SNo": "Item-124", "Name": "Pen", "Cost": 12},
    {"SNo": "Item-125", "Name": "Book", "Cost": 50},
    {"SNo": "Item-126", "Name": "Ink", "Cost": 25},
    {"SNo": "Item-127", "Name": "Paper", "Cost": 3},
    customerId = 9876, customerName = "Hope", customerAge = 30
)