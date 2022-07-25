#This program was a industry question in an interview
#Question is to enter Currency denominations for eg. [5,6,9] and target value for eg. 11. the program then should generate change from the list i.e 5, 6 =11
#Code is incomplete as of now for the second part


currency = []

def appendFunction():
    totalDenom = int(input("Enter total number of Denominations: "))
    count = 1
    while totalDenom >= count:
        value = int(input("Enter Denomination " + str(count) + " : "))
        currency.append(value)
        count += 1
    showCurrency = input(print("display denominations Value? y/n : "))
    if showCurrency.upper() == "Y":
        print(currency)


def removeFunction():
    showCurrency = input(print("display denominations Value? y/n : "))
    if showCurrency.upper() == "Y":
        print(currency)
    else:
        removeWhat = int(input("Remove what denomination?: "))
        index = currency.index(removeWhat)
        currency.remove(index)
        print(str(removeWhat) + "Was Removed from the List")

def changeFunction(targetValue):
    count = len(currency)
    loopCount = 1
    index_zero = 0 - count
    index = 0
    while index >= -6:
        index = -1

        


print("Loading...")


while True:
    print("Welcome to Change allocator")
    reset = input(print("Do you want to Reset or Add or Remove a Denomination(s) or Generate change? reset/add/remove/change/exit: "))
    if reset.upper() == "RESET":
        currency.clear()
        add = input(print("Database Reseted! Do you want to add new Denominations? y/n :"))
        if add.upper() == "Y":
            appendFunction()
    elif reset.upper() == "ADD":
        appendFunction()
    elif reset.upper() == "REMOVE":
        removeFunction()
    elif reset.upper() == "CHANGE":
        targetValue = int(input(print("Enter Target Value: ")))
        changeFunction(targetValue)
    else:
        exit = input(print("Input error - Try Again or type exit or press enter"))
        if exit.upper() == "EXIT":
            break
        else:
            continue
print("Thank you for using Pathak's Change Generator")