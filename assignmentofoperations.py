print("_______________________________________________________________________________")
print("|  ###### ####### ####### ####### ###### ####### ## ###### ####    ## ######  |")
print("|  ##  ## ##   ## ##      ##   ## ##  ##   ##    ## ##  ## ## ##   ## ##      |")
print("|  ##  ## ####### ####### ####### ######   ##    ## ##  ## ##  ##  ## ######  |")
print("|  ##  ## ##      ##      ##  ##  ##  ##   ##    ## ##  ## ##   ## ##     ##  |")
print("|  ###### ##      ####### ##   ## ##  ##   ##    ## ###### ##    #### ######  |")
print("|_____________________________________________________________________________|")        
num1 = int(input('            Enter First Number: '))
num2 = int(input('            Enter Second Number: '))
operation = input('        Please Provide An Operand(+ , - , * , / ): ')
if operation == "+":
    total = num1+num2
    print("Result is~~~")
    print(total)
elif operation == "-":
    total = num1-num2
    print('Result is~~~')
    print(total)
elif operation == "*":
    total = num1*num2
    print('Result is~~~')
    print(total)
elif operation == "/":
    total = num1/num2
    print('Result is~~~')
    print(total)
else:
    print('You have given wrong operation')

