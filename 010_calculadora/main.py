def add(number_1, number_2):
    return number_1 + number_2


def subtract(number_1, number_2):
    return number_1 - number_2


def multiply(number_1, number_2):
    return number_1 * number_2


def divide(number_1, number_2):
    return number_1 / number_2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    execute = True
    first_number = float(input("What's the first number?: ")) 

    while execute:

        

        print("Mathemtatical operations:")
        for i in operations:
            print(i)

        operation = input("Pick an operation: ")

        second_number = float(input("What's the second number?: "))

        result = operations[operation](number_1=first_number, number_2=second_number)

        print(f"{first_number} {operation} {second_number} is: {result}")

        new_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if new_calculation == 'y':
            first_number = result
        else:
            execute = False
            calculator()
    


calculator()




