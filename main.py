def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
keep_going = True
num1 = float(input("What's the first number?: "))

while keep_going:
    for operand in operators:
        print(operand)
    operation_symbol = input("Pick an operation symbol from the line above: ")
    num2 = float(input("What's the next number?: "))
    answer = operators[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    state = input(f"Do you want to continue calculations with {answer}? type 'y' or 'n' ").lower()
    if state != "y":
        keep_going = False
    else:
        num1 = answer
