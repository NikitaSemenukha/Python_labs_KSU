"""
12. Дано чотири цілих числа, одне з яких відмінно від трьох інших, рівних між собою. Вивести
порядковий номер цього числа.
"""


def main(num_1, num_2, num_3, num_4):
    if num_2 == num_3 == num_4 != num_1:
        return 1
    if num_1 == num_3 == num_4 != num_2:
        return 2
    if num_1 == num_2 == num_4 != num_3:
        return 3
    if num_1 == num_2 == num_3 != num_4:
        return 4
    else:
        return 'False'


print('Введіть чотири цілих числа:')
n_1 = int(input('x1 = '))
n_2 = int(input('x2 = '))
n_3 = int(input('x3 = '))
n_4 = int(input('x4 = '))
if __name__ == '__main__':
    result = main(n_1, n_2, n_3, n_4)
    print(result)