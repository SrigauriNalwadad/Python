#Simple Function
def greet():
    print("Hello World!")
    print("Python coding is fun.")
    print("100 Days of Coding.")
greet()

#Function with Input
def greet_with_name(name):
    print(f"\nHello {name}")
    print("Python coding is fun.")
    print("100 Days of Coding.")
greet_with_name('Gauri')

#Functions with more inputs
def add(a,b,c):
    return int(a)+int(b)+int(c)
sum = add(1,2,3)
print(f"\nAddition = {sum}")
