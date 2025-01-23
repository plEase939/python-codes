#This program was a industry question in an interview
#Question is to enter Currency denominations for eg. [5,6,9] and target value for eg. 11. the program then should generate change from the list i.e 5, 6 =11
currency = []
user_input = input("Do you want to load default Indian Currency set? y/n: ")
if user_input.lower() == "y":
    currency = [500, 100, 50, 20, 10, 5, 2, 1]
else:
    total_inputs = int(input("How many denominations do you want to enter?: "))
    for x in range(total_inputs):
        user_input = int(input(f"Enter your {x+1} Currency denomination (as integer): "))
        currency.append(user_input)
    currency.sort(reverse=True)

while True:
    try:
        user_input = input("Disperse change for the amount of or type 0 to exit: ")
        if user_input == "0":
            break
        user_amount = int(user_input)
        
        temp = user_amount
        index = 0
        while temp > 0:
            i = 0
            while temp >= currency[index]:
                temp -= currency[index]
                i += 1
            if i > 0:
                print(f"{i} Note(s) of {currency[index]}")
            index += 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
