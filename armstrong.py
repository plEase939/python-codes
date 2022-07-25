


def threeDigit(Value):
    temp = Value
    temp = temp / 100
    temp = int(temp) *100
    print(temp)

Value = int(input("Enter three digit number: "))
threeDigit(Value)