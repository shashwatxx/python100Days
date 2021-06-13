from calArt import logo


print(logo)


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def muliply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operation_dict = {
    "+": add,
    "-": subtract,
    "*": muliply,
    "/": divide
}


def calculate():
    should_continue = True
    first = float(input("What's the First Number? : "))
    for symbol in operation_dict:
        print(symbol, end=" ")
    while should_continue:
        operation_symbol = input("Pick an operation : ")
        second = float(input("What's the Next Number? : "))
        calculation_funtion = operation_dict[operation_symbol]
        answer = calculation_funtion(first, second)
        print(f"{first} {operation_symbol} {second} = {answer}")
        if input(f"Type 'y' to continue calclulating with {answer},or type 'n' to exit: ").lower() == "y":
            first = answer
        else:
            should_continue = False


calculate()
