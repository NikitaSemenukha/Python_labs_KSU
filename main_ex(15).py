"""
15. Дано змінні A, B, C. Змінити їх значення, перемістивши вміст A в B, B - в C, C - в A, і вивести
нові значення змінних A, B, C.
"""


def main():
    A = float(input('A = '))
    B = float(input('B = '))
    C = float(input('C = '))

    A, B, C = B, C, A
    print('A = ', A)
    print('B = ', B)
    print('C = ', C)


if __name__ == '__main__':
    main()