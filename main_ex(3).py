"""
Дано два ненульових числа. Знайти суму, різницю, добуток і частку їх квадратів
"""

def check(x, y):                                                  #функция проверки числа на неравноесть 0
    if x == 0 or y == 0:
        print('Error')
    else:
        operations(x, y)


def operations(x, y):                                             #функция вычисления операций квадратов 2 чисел
    print('Summa = ',       (x ** 2) + (y ** 2))
    print('Difference',     (x ** 2) - (y ** 2))
    print('Multiplication', (x ** 2) * (y ** 2))
    print('Division',       (x ** 2) / (y ** 2))

def main():
    a = float(input('Enter first value: '))
    b = float(input('Enter second value: '))
    check(a, b)                                                       #Вызов функции check

if __name__ == '__main__':
    main()