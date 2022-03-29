"""
16. Визначити число, яке отримано записом у зворотньому порядку цифр заданого тризначного
числа.
"""

import random


def check_0(numb):
    if (numb > 99) and (numb < 1000):
        calc(numb)
    else:
        print('Error')


def calc(numb):
    a = numb % 10
    b = (numb % 100) // 10
    c = numb // 100
    numb_1 = b * 100 + c * 10 + a
    numb_2 = c * 100 + a * 10 + b
    numb_3 = a * 100 + b * 10 + c
    shuffle(numb_1, numb_2, numb_3)


def shuffle(numb_1, numb_2, numb_3):
    array = [numb_1, numb_2, numb_3]
    random.shuffle(array)
    for i in array:
        print(i, end=' ')
    question(array, numb_3)


def question(array, numb_3):
    print('\nЯке число отримано записом у зворотньому порядку?')
    print('1 2 3\n')
    a = int(input(''))
    mixing(a, array, numb_3)


def mixing(b, arr, num_3):
    if b == 1 or b == 2 or b == 3:
        if arr[0] == num_3 and b == 1:
            print('True')

        if arr[1] == num_3 and b == 2:
            print('True')

        if arr[2] == num_3 and b == 3:
            print('True')
    else:
        print('Відповідь неправильна або невірно вказано цифру')


def main():
    x = int(input('Enter the number: '))
    check_0(x)


if __name__ == '__main__':
    main()
