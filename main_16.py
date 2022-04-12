"""
16. Дано ціле число, що позначає код символу по таблиці ASCII. Визначити, це код англійської
літери або будь-якої іншої символ.
"""


def main(def_value):
    if 0 <= def_value <= 255:
        if 65 <= def_value <= 90 or 97 <= def_value <= 122:
            return f'Це код англійської літери {chr(def_value)}'
        else:
            return f'Це код англійської літери {chr(def_value)}'
    else:
        return 'Невірно вказано число'


print('Введіть ціле число з діапазону 0 - 255')
value = int(input(''))
if __name__ == '__main__':
    result = main(value)
    print(result)