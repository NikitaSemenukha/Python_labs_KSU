"""
6. Логічній змінній t присвоїти значення true або false залежно від того, є натуральне число k
ступенем 3 чи ні.
"""


import math


def main(value):
    t = 0
    power = 0
    i = 1
    while power < value:
        power = math.pow(3, i)
        if power == value:
            t = 1
        i += 1
    if t == 1:
        return 'True'
    else:
        return 'False'


print('Enter the value:')
val = int(input(''))
if __name__ == '__main__':
    result = main(val)
    print(result)