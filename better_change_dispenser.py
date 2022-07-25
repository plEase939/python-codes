#This program was a industry question in an interview
#Question is to enter Currency denominations for eg. [5,6,9] and target value for eg. 11. the program then should generate change from the list i.e 5, 6 =11
#Code is incomplete as of now for the second part

currency = (2000, 500, 100, 50, 20, 10 , 5, 2, 1)


def dispense(targetValue):
   
    tempValue = targetValue
    if tempValue >= 2000:
        count2000 = 0
        while tempValue >= 2000:
            tempValue = tempValue - currency[0]
            count2000 += 1
        print(str(count2000) + " Note(s) of 2000")
    if tempValue >= 500:
        count500 = 0
        while tempValue >= 500:
            tempValue = tempValue - currency[1]
            count500 += 1
        print(str(count500) + " Note(s) of 500")
    if tempValue >= 100:
        count100 = 0
        while tempValue >= 100:
            tempValue = tempValue - currency[2]
            count100 += 1
        print(str(count100) + " Note(s) of 100")
    if tempValue >= 50:
        count50 = 0
        while tempValue >= 50:
            tempValue = tempValue - currency[3]
            count50 += 1
        print(str(count50) + " Note(s) of 50")
    if tempValue >= 20:
        count20 = 0
        while tempValue >= 20:
            tempValue = tempValue - currency[4]
            count20 += 1
        print(str(count20) + " Note(s) of 20")
    if tempValue >= 10:
        count10 = 0
        while tempValue >= 10:
            tempValue = tempValue - currency[5]
            count10 += 1
        print(str(count10) + " Note(s)/Coins of 10")
    if tempValue >= 5:
        count5 = 0
        while tempValue >= 5:
            tempValue = tempValue - currency[6]
            count5 += 1
        print(str(count5) + " Coins of 5")
    if tempValue >= 2:
        count2 = 0
        while tempValue >= 2:
            tempValue = tempValue - currency[7]
            count2 += 1
        print(str(count2) + " Coin(s) of 2")
    if tempValue >= 1:
        count1 = 0
        while tempValue >= 1:
            tempValue = tempValue - currency[8]
            count1 += 1
        print(str(count1) + " Coin(s) of 1")
            






while True:
    print("Welcome to Pathak's Change Dispenser")
    targetValue = int(input("Please input the amount you want to withdraw: "))
    print("\n")
    dispense(targetValue)
    print("Change Generated \n")




