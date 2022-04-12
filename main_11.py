"""
11. Дано три змінні: X, Y, Z. Якщо їх значення впорядковані за спаданням, то подвоїти їх; в іншому
випадку замінити значення кожної змінної на протилежне.
"""


def main(def_x, def_y, def_z):
    if def_x > def_y > def_z:
        return def_x * 2, def_y * 2, def_z * 2
    else:
        return def_x * (-1), def_y * (-1), def_z * (-1)


print('Введіть х, у, z:')
x_0 = float(input('x = '))
y_0 = float(input('y = '))
z_0 = float(input('z = '))
if '__main__' == __name__:
    result = main(x_0, y_0, z_0)
    print(result)



