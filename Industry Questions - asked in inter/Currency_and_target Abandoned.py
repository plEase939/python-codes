#This program was a industry question in an interview
#Question is to enter Currency denominations for eg. [5,6,9] and target value for eg. 11. the program then should generate change from the list i.e 5, 6 =11
#Code is incomplete as of now for the second part


currency =[]


def currencyAdd(totalDenom):
    reset = input("Do you want to reset the database or add or remove a denomination(s)")
    if reset.upper() == "RESET":
        currency.clear()
    elif reset.upper() == "ADD":
        

    count = 1
    while totalDenom >= count:
        value = int(input("Enter Denomination " + str(count) + " : "))
        currency.append(value)
        count += 1

def Target(targetValue):
    if targetValue == 0:
        print("No changed as value is 0")
    
while True:
    totalDenom = int(input("Enter total number of Denominations: "))
    call = input("Add/Update/remove new denominations to the memory? y/n :  ")
    if call.upper() == "Y":
        currencyAdd(totalDenom)
    else:
        print("Rejected by user")

    print(currency)

    quest = input("Do you want to put a target Value to generate Change? y/n:  ")
    if quest.upper() == "Y":
        targetValue = int(input("Enter Target Value: "))
        Target(targetValue)
    else:
        print("Rejected by user")



