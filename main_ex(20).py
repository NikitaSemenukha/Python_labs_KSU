"""
20. Присвоїти цілій змінній d першу цифру з дробової частини позитивного дійсного числа x.
"""


def main():
    x = float(input('x = '))
    x *= 10             #переводимо першу цифру дробової частини в цілу
    d = int(x)          #відкидаємо залишок дробової частини
    d %= 10             #відділяємо останню цифру
    print('d = ', d)


if __name__ == '__main__':
    main()