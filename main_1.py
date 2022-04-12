"""
1. Підрахувати k - кількість цифр в десятковому запису цілого невід'ємного числа n.
"""


print('Enter the int value:')
val = int(input(''))
if val > 0:
    print(len(str(val)))
else:
    print('Error')