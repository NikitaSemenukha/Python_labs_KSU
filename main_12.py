"""
12. Дано дійсне число - ціна 1 кг цукерок. Вивести вартість 1, 2, ..., 10 кг цукерок.
"""


print('Введіть вартість 1 кг цукерок')
cost = float(input('Ціна за кілограмм '))
if cost > 0:
    n = 10
    i = 1
    while n > 0:
        print(i, 'кг цукерок коштує', cost * i, 'грн')
        i += 1
        n -= 1
else:
    print('Невірно введена ціна')