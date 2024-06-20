def eval_op(op, a, b):
    if op == '#':
        return 4 * a + 3 * b + 2
    elif op == '$':
        return 2 * a + b + 3
    else:
        raise ValueError(f"Unknown operator: {op}")

def precedence(op):
    if op == '#':
        return 2  # Higher precedence
    elif op == '$':
        return 1  # Lower precedence
    return 0

def apply_ops(operands, operators):
    b = operands.pop()
    a = operands.pop()
    op = operators.pop()
    operands.append(eval_op(op, a, b))

def mars_operations(expression):
    operands = []
    operators = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            val = 0
            while (i < len(expression) and expression[i].isdigit()):
                val = (val * 10) + int(expression[i])
                i += 1
            operands.append(val)
            i -= 1
        else:
            while (len(operators) != 0 and
                   precedence(operators[-1]) >= precedence(expression[i])):
                apply_ops(operands, operators)
            operators.append(expression[i])
        i += 1

    while len(operators) != 0:
        apply_ops(operands, operators)

    return operands[-1]

# Example usage:
expression = "2#3$4"
result = mars_operations(expression)
print(f"The result of the expression '{expression}' is: {result}")
