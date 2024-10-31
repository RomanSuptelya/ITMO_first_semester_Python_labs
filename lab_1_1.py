
'''Вариант 1'''


'''ЗАДАНИЕ 1 (Флаг Франции)'''


RED = '\x1b[48;5;196m' # 48;5 - обязательная часть, далее число от 0 до 255
# коды цветов: https://dvmn.org/encyclopedia/python_strings/ansi-codes/
BLUE = '\x1b[48;5;21m'
WHITE = '\x1b[48;5;255m'
END = '\x1b[0m' # сброс цвета

LENGTH = 9 # Длина флага
WIDTH = 6 # Ширина флага

# print(RED + '*'*10 + END) # строка 7 и 8 равны
# print(f'{RED}{'*'*10}{END}')


for j in range(WIDTH):
        if __name__ == '__main__':  # запуск программы
                print(f'{BLUE}{' '*LENGTH}{WHITE}{' '*LENGTH}{RED}'
                      f'{' '*LENGTH}{END}')
