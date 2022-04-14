"""
12. Написати програму циклічного зсуву елементів списку вліво. Наприклад, дано список:
[1,2,3,4,5,6] після зсуву на один елемент вліво, повинні отримати: [2,3,4,5,6,1].
"""


def main(len_: list):
    return [len_.pop()] + len_


lst_ = []
for i in range(int(input())):
    lst_.append(int(input()))
if __name__ == '__main__':
    print(main(lst_))
input()