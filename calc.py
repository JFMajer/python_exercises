import operator

operators = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "%": operator.mod,
    "**": operator.pow
}


def calc(operation: str):
    parts = operation.split(maxsplit=2)
    operand = parts[0]
    num1 = float(parts[1])  # Convert the second part to float
    num2 = float(parts[2])  # Convert the third part to float
    return operators[operand](num1, num2)


print(calc("+ 2 3"))
print(calc("** 2 3"))