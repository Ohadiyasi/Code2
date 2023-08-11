from math import sin, cos, radians, tan, factorial, sqrt
import sys

operand_1 = float(input('Type the first number: '))

simpleOperators = ['+', '-', '*', '/']
complexOperators = [ 'sin', 'cos', 'tan', 'cot', 'factorial', 'radical']
operators = simpleOperators + complexOperators
message = ''

for char in operators:
    message += char + ', '
operator = input(f'Choose the operator from ({message}): ')

if operator in complexOperators:
    if operator == 'sin':
        result = sin(radians(operand_1))
    if operator == 'cos':
        result = cos(radians(operand_1))
    if operator == 'tan':
        result = tan(radians(operand_1))
    if operator == 'cot':
        result = 1/tan(radians(operand_1))
    if operator == 'factorial':
        result = factorial(operand_1)
    if operator == 'radical':
        if operand_1 < 0: raise ValueError
        else: result = sqrt(operand_1)

else:
    operand_2 = float(input('Type the second number: '))

    if operator == '+':
        result = operand_1 + operand_2
    elif operator == '-':
        result = operand_1 - operand_2
    elif operator == '*':
        result = operand_1 * operand_2
    elif operator == '/':
        result = operand_1 / operand_2

result = str(result)
print('the answer is: ' + result)