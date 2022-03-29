"""
18. Розв'язати лінійне рівняння A · x + B = 0, задане своїми коефіцієнтами A і B (коефіцієнт A НЕ
дорівнює 0).
"""


def check(A, B):
    if A == 0:
        print('Error')
    else:
        calc(A,B)


def calc(A, B):
    x = (-B/A)
    print("Розв'язком рівняння Ax + B = 0, є число ", x)


def main():
    A = float(input('A = '))
    B = float(input('B = '))
    check(A, B)


if __name__ == '__main__':
    main()