"""
11. Дано цілі числа K і N (N> 0). Вивести N раз число K.
"""


print('Enter integer (N > 0), K')
N = int(input('N = '))
K = int(input('K = '))
if N > 0:
    while N != 0:
        print(K)
        N -= 1