"""
12. Дано значення кута α в градусах (0 ≤ α < 360). Обчислити значення цього ж кута в радіанах,
враховуючи, що 180 ° = π радіанів. У якості значення π використовувати 3.14.
"""


def check(Angle):                                           #функція перевірки кута у діапазоні (0 ≤ α < 360).
    if Angle >= 0 and Angle <= 360:
        calc(Angle)
    else:
        print('Error')


def calc(Angle):                                            #функція обрахунку кута у радіанах
    Radian = Angle * 3.14 / 180
    print('Radian = ', Radian)


def main():
    ang = float(input('Enter the angle:'))                      #вводимо дані з клавіатури та викликаємо функцію check3
    check(ang)


if __name__ == '__main__':
    main()
