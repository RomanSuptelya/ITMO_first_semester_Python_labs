
'''Вариант 1'''


'''ЗАДАНИЕ 3 (Парабола)'''


SET_COLOR = '\x1b[48;5;202m' # Установить цвет
CLEAR_COLOR = '\x1b[0m'  # Сбросить цвет
LINE = ' '


def draw_line(offset=0): # печатает 1 прямоугольник
    #offset = 0 # отступ от края

    print(f"{' ' * offset}{SET_COLOR}{LINE}{CLEAR_COLOR}")


def draw_parabola():
    for i in range(100, -1, -10):
        offset = round(i ** 0.5)
        draw_line(offset)


if __name__ == '__main__':
    draw_parabola()

