"""
    1. Дана сторона квадрата a. Знайти його периметр P=4·a.
    2. Дана сторона квадрата a. Знайти його площу S=a2
"""

def main():
    side = float(input("Enter side of square: "))                                           #вводимо дані з клавіатури
    print( 'Perimetr of square = ', side * 4, 'and square square = ', side ** 2 )           #вивід даних

if __name__ == '__main__':
    main()