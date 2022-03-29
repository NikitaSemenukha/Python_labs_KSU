"""
9. Дано двозначне число. Знайти суму і добуток його цифр.
"""


def check(a):                                       #перевірка числа
    if (a > 9) and (a < 100):
        calc(a)
    elif (a > -100) and (a < -9):
        calc(a * (-1))
    else:
        print('Error')


def calc(b):                                        #функція обчислення суми і добутку  цифр числа
    a = b // 10                                     #ділення націло
    c = b % 10                                      #остача від ділення
    print('Suma = ',           a + c)
    print('Multiplication = ', a * c)


def main():
    num = int(input('Enter the number: '))              #вводимо дані з клавіатури
    check(num)


if __name__ == '__main__':
    main()