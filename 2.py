import sys
import termcolor2 as clr

a, b, c = input('type three numbers: (format: 1, 2, 3) ').split(',')

numbers = [int(a), int(b), int(c)]
numbers.sort()

for i in range(3):
    operand = numbers.pop()
    if operand >= sum(numbers):
        print(clr.colored('No triangle allowed!', color = 'red'))
        sys.exit()
    else:
        numbers.insert(0, operand)

print(clr.colored('Triangle allowed!', color = 'cyan'))
