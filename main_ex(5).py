"""
5. Обчислити дробову частину середнього геометричного трьох заданих позитивних чисел.
"""
import math                                                  #імпортуємо бібліотеку math


def check(a, b, c):                                          #функція перевірки чисел на позитивність
    if a > 0 and b > 0 and c > 0:
        geometricAverage(a, b, c)
    else:
        print('Error')


def geometricAverage(x, y, z):                               #функція знаходження дробової частини для 3 позитивних чисел
    geometric_average = (x * y * z) ** (1/3)
    print('Geometric average of three numbers =', geometric_average - math.floor(geometric_average))

def main():
    num_1 = float(input('Enter first value: '))                  #вводимо дані з клавіатури
    num_2 = float(input('Enter second value: '))
    num_3 = float(input('Enter third value: '))
    check(num_1, num_2, num_3)                                   #викликаємо функцію check


if __name__ == '__main__':
    main()