"""
8. Відомо, що X кг цукерок коштують A гривень. Визначити, скільки коштує 1 кг і Y кг цих же
цукерок - можливо умова неповна, в інтернеті я знайшов подібну умову
"""
"""
 Відомо, що x кг цукерок коштують a гривень. 
 Визначте, скільки коштує y кг цих цукерок, а також скільки кг цукерок можна купити на k гривень. Всі значення вводить користувач.
 """

class Shop(object):

    def check(x, cost):
        if x > 0 and cost > 0:
            calculation(x, cost)
        else:
            print('Error')

def calculation(x, cost):



X = float(input('Скільки кілограммів цукерок хочете купити? \n'))
summa = float(input('Яку сумму грошей плануєте витратити? \n'))
check(X, summa)
print()