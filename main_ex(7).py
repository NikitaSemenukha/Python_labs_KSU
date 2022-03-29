"""
7. За довжинами двох сторін деякого трикутника і кутом між ними знайти довжину третьої сторони і
площу цього трикутника.
"""

#Программа іноді видає помилку типу Traceback (most recent call last): наприклад 15, 16, 75
import math                                                                 #імпортуємо бібліотеку math


def check(side_A, side_B, Angle):                                           #функція перевірки
    if side_A > 0 and side_B > 0 and (Angle > 0 or Angle < 180):
        triangle(side_A, side_B, Angle)
    else:
        print('Error')


def triangle(side_1, side_2, A):                                            #функція прорахунку через т.косинусів третю сторону та площі за формулою Герона
    side_3 = math.sqrt(side_1 ** 2 + side_2 ** 2 - 0.5 * side_1 * side_2 * (math.cos(A)))
    p = (side_1 + side_2 + side_3) / 3
    Square_tr = math.sqrt(p * (p - side_1) * (p - side_2) * (p - side_3))
    print('Side_AC = ', side_3)
    print('Square = ', Square_tr)


def main():
    side_AB = float(input('Enter side AB:'))
    side_AC = float(input('Enter side AC:'))
    angle = float(input('Enter angle(AB,AC):'))                              #вводимо дані з клавіатури
    check(side_AB, side_AC, angle)                                           #виклик функції


if __name__ == '__main__':
    main()