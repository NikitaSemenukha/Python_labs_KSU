"""
6. Поміняти місцями вміст змінних A і B і вивести нові значення A і B.
"""


def Swap(a, b):                     #функція зміни місцями змінних
    a, b = b, a
    """
    a = a + b  
    b = a - b  
    a = a - b  
    """
    print(' x = ', a)
    print(' y = ', b)


def main():
    x = float(input("x = "))
    y = float(input("y = "))
    Swap(x, y)


if __name__ == '__main__':
    main()

