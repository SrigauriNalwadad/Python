#Calculator

#Addition
def add(n1,n2):
    return n1 + n2

#Subtraction
def subtract(n1,n2):
    return n1 - n2

#Multiplication
def multiply(n1,n2):
    return n1 * n2

#Division
def division(n1,n2):
    if n2==0:
        print("Division not possible.")
    else:
        return n1 / n2

#Creating Dictionary
operations = {"+" : add,"-" : subtract,"*" : multiply,"/" : division}

num1 = int(input("What is your first number?: "))
num2 = int(input("What is your second number?: "))

for symbol in operations:
    print(symbol)

operational_symbol = input("Choose a symbol from above to prefrom operation: ")
calculation_function = operations[operational_symbol]
answer = calculation_function(num1,num2)

print(f"{num1} {operational_symbol} {num2} = {answer}")
