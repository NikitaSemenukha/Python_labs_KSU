"""
4. Дано катети прямокутного трикутника a і b. Знайти його гіпотенузу c і периметр
"""

import math                                                     #імпортуємо бібліотеку math


def check(a, b):                                                #функція перевірки катетів трикутника
    if a > 0 and b > 0:
        triangle(a, b)
    else:
        print('Error')


def triangle(a, b):                                             #функція знаходження гіпотенузи та периметра трикутника
    c = math.sqrt((a ** 2) + (b ** 2))
    print('Hypotenuse = ', c)
    print('Perimeter = ',   a + b + c)


def main():
    leg_1 = float(input('Enter first leg: '))                        #вводмо дані з клавіатури
    leg_2 = float(input('Enter second leg: '))
    check(leg_1, leg_2)                                             #виклик функції check


if __name__ == '__main__':
    main()