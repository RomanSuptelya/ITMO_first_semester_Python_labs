
'''Вариант 1'''


'''ЗАДАНИЕ 4 (График кол-во чисел меньше и больше 0)'''


ORANGE = '\x1b[48;5;202m' # оранжевый цвет
BLUE = '\x1b[48;5;45m' # голубой цвет
CLEAR_COLOR = '\x1b[0m' # очистить цвет
SCALE = 2 # масштаб графика

with open('sequence') as file: # открыть файл
    count_positive_numbers = 0 # кол-во положительных чисел
    count_negative_numbers = 0 # кол-во отрицательных чисел

    for line in file:
        number = float(line) # переводи числа из float в int
        if number > 0: # счет если число положительное
            count_positive_numbers = count_positive_numbers + 1
        elif number < 0: # счет если число отрицательное
            count_negative_numbers = count_negative_numbers + 1


if __name__ == '__main__':
    print(f'{ORANGE}{' '*(count_positive_numbers // SCALE)}{CLEAR_COLOR}'
          f'{' '}{count_positive_numbers}{' '}{'положительные'}')
    print(f'{BLUE}{' '*(count_negative_numbers // SCALE)}{CLEAR_COLOR}'
          f'{' '}{count_negative_numbers}{' '}{'отрицательные'}')


