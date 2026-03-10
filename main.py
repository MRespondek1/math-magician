# Math Magician Main File
# usage: python3 math.py <operator> <operand1> <operand2>
import sys


def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 math.py <operator> <number1> <number2>")
        return

    print("Welcome to Math Magician")

    op = sys.argv[1]
    
    try:
        a = float(sys.argv[2])
        b = float(sys.argv[3])
    except ValueError:
        print("Error: Operands must be numbers.")
        return

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        if b == 0:
            print("Error: Division by zero")
            return
        result = div(a, b)
    else:
        print("Invalid operator: use +, -, *, or /")
        return

    print(result)

if __name__ == "__main__":
    main()
