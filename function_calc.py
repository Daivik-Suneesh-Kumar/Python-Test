def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

try:
    a = float(input("Enter your first number."))
    b = float(input("Enter your second number."))
    operation = str(input("Which operation do you want to use? (Add,Sub,Mul,Div)")).upper()
    if operation == "ADD":
        result = add(a,b)
        print("Result:",result)
    elif operation == "SUB":
        result = sub(a,b)
        print("Result:",result)
    elif operation == "MUL":
        result = mul(a,b)
        print("Result:",result)
    elif operation == "DIV":
        result = div(a,b)
        print("Result:",result)
    else:
        print("Invalid operation.")
except ZeroDivisionError:
    print("You cannot divide a number by 0.")
except ValueError:
    print("Wrong value entered. Please enter a number.")
    

