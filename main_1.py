"""
1. Дано ціле число. Якщо воно є додатним, то відняти від нього 8; в іншому разі не змінювати його.
Вивести отримане числ
"""


def main(a):
    if a > 0:
        a -= 8
        return a
    else:
        return a


if __name__ == "__main__":
    result = main(int(input('a = ')))
    print(result)