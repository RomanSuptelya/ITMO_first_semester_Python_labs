
'''Вариант 1'''


'''ВТОРОЕ ЗАДАНИЕ (Узор шахматы)'''


import time

SET_COLOR = '\x1b[48;5;' # Установить цвет
CLEAR_COLOR = '\x1b[0m'  # Сбросить цвет
SIDE = 2 # масштаб узора


def draw_line(color): # печатает 1 узор

    length = ' ' * 3 * SIDE  # длина квадратика
    width = SIDE  # высота квадратика

    for i in range(width): # 1-ая строка узора
        print(f'{SET_COLOR}{color}m{length}{CLEAR_COLOR}{length}'
              f'{SET_COLOR}{color}m{length}{CLEAR_COLOR}')
    for i in range(width): # 2-ая строка узора
        print(f'{length}{SET_COLOR}{color}m{length}{CLEAR_COLOR}')
    for i in range(width): # 3-ая строка узора
        print(f'{SET_COLOR}{color}m{length}{CLEAR_COLOR}{length}'
              f'{SET_COLOR}{color}m{length}{CLEAR_COLOR}')
    print(f'\u001b[{SIDE*3}A', end='') # переместить курсор наверх


def draw_chess():
    colors = [202, 45]
    for i in range(1): # while True - бесконечный цикл
        for color in colors: # смена цветов
            draw_line(color) # go to def draw_line
            time.sleep(3) # задержка по времени


if __name__ == "__main__": # запуск программы
        draw_chess()
