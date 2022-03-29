"""
13. Дані координати двох протилежних вершин прямокутника: (x1, y1), (x2, y2). Сторони
прямокутника паралельні до осів координат. Знайти периметр і площу даного прямокутника.
"""
import math                                                         #підключаємо бібліотеку math


def rectangle(x1, y1, x2, y2):                                      #функція для обрахунку площі та периметру прямокутника
    AB = math.sqrt(((2 * x2) ** 2) + ((2 * y1) ** 2))               #знаходимо сторони прямокутника
    AC = math.sqrt(((2 * x1) ** 2) + ((2 * y2) ** 2))
    Square = AB * AC
    Perimeter = 2 * (AB + AC)                                       #знаходимо периметр та площу прямокутника та виводимо їх на екран
    print('Square rectangle = ', Square)
    print('Perimeter of rectangle = ', Perimeter)


def main():
    x1 = float(input('x1 = '))
    x2 = float(input('x2 = '))
    y1 = float(input('y1 = '))                                      #вводимо дані з клавіатури та викликаємо функцію rectangle
    y2 = float(input('y2 = '))
    rectangle(x1, y1, x2, y2)


if __name__ == '__main__':
    main()