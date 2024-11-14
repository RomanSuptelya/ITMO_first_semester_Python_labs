
'''Вариант 1'''


'Все открывающие теги без повторений.'


import re

with open('task2.html') as file:
    n = 0  # счетчик номера строки
    for line in file:
        n = n + 1  # счетчик номера строки
        res = re.findall(r'<[aA-zZ]{1,}.{0,}?>',line)
            # . - любой символ
            # ? - берем первое попавшееся вхождение

        if __name__ == '__main__':
            print(n, res)