import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }
#print (operations["*"](4,8))
def calculator():
    print(art.logo)
    should_accomulate = True
    num1 = float(input("What is the first number?"))
    while should_accomulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number?"))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"type ´Y´ to continue calculatiing with {answer}, or type `N` to start a new calculation.")

        if choice == "y":
            num1 = answer
        else:
            should_accomulate = False
            print("/n" * 20)
            calculator()

calculator()
