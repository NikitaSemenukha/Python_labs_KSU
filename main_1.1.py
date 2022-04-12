"""
1. Підрахувати k - кількість цифр в десятковому запису цілого невід'ємного числа n.
"""


import math


def main(value):
    if value > 0:
        return int(math.log10(value)) + 1
    elif value == 0:
        return 1
    elif value < 0:
        return int(math.log10(-value)) + 1


print('Enter an integer:')
val = int(input(''))
if __name__ == '__main__':
    result = main(val)
    print(result)