#This program was a industry question in an interview
#Question is to enter Currency denominations for eg. [5,6,9] and target value for eg. 11. the program then should generate change from the list i.e 5, 6 =11
curreny = []

total_inputs = int(input("How many demoninations you want to enter?: "))
for x in range(0,total_inputs):
    print("Enter your ", x+1, "Currency: ")
    user_input = int(input())
    curreny.append(user_input)

curreny.sort(reverse=True)

while True:
    user_action = input("Continue? y/n ")
    if user_action.upper() == "N":
        break
    else:
        user_amount = int(input("Disperse change for the amount of: "))
        temp = user_amount
        index = 0
        while temp > 0:
            i = 0
            while temp >= curreny[index]:
                temp = temp - curreny[index]
                i += 1
            print(i, "Note(s) of ", curreny[index])
            index += 1
