
'''Вариант 1'''


'Все слова от 3 до 5 букв; все числа больше 3 знаков.'


import re

with open('task1-en') as file:
    n = 0 # счетчик номера строки
    for line in file:
        n = n + 1 # счетчик номера строки
        res = re.findall(r'\b[aA-zZ]{3,6}\b|' # все слова от 3 до 5 букв
                                r'\d{3,}' # все числа больше 3 знаков
                                ,line)


        print(n, res)