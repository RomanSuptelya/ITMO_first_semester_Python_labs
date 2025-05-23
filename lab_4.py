
'''Вариант 1'''


'2x4'


stuffdict = {'r':(3, 25),
             'p':(2, 15),
             'a':(2, 15),
             'm':(2, 20),
             'k':(1, 15),
             'x':(3, 20),
             't':(1, 25),
             'f':(1, 15),
             's':(2, 20),
             'c':(2, 20)
             }

def get_area_and_value(stuffdict): #создаем списки только из площади и только
    # из ценности
    area = [stuffdict[item][0] for item in stuffdict]
    value = [stuffdict[item][1] for item in stuffdict]
    return area, value


def get_memtable(stuffdict, A=8): #n - всего предметов, A - максимальная
    # допустимая площадь
    area, value = get_area_and_value(stuffdict)
    n = len(value)  # находим размеры таблицы

    # создаём таблицу из нулевых значений
    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            # базовый случай
            if i == 0 or a == 0:
                V[i][a] = 0

            # если площадь предмета меньше площади столбца,
            # максимизируем значение суммарной ценности
            elif area[i - 1] <= a:
                V[i][a] = max(value[i - 1] + V[i - 1][a - area[i - 1]],
                              V[i - 1][a])

            # если площадь предмета больше площади столбца,
            # забираем значение ячейки из предыдущей строки
            else:
                V[i][a] = V[i - 1][a]
    return V, area, value


def get_selected_items_list(stuffdict, A=8):
    V, area, value = get_memtable(stuffdict)
    n = len(value)
    res = V[n][A]  # начинаем с последнего элемента таблицы
    a = A  # начальная площадь - максимальная
    items_list = []  # список площадей и ценностей

    for i in range(n, 0, -1):  # идём в обратном порядке
        if res <= 0:  # условие прерывания - собрали "рюкзак"
            break
        if res == V[i - 1][a]:  # ничего не делаем, двигаемся дальше
            continue
        else:
            # "забираем" предмет
            items_list.append((area[i - 1], value[i - 1]))
            res -= value[i - 1]  # отнимаем значение ценности от общей
            a -= area[i - 1]  # отнимаем площадь от общей

    selected_stuff = []

    # находим ключи исходного словаря - названия предметов
    for search in items_list:
        for key, value in stuffdict.items():
            if value == search:
                selected_stuff.append(key)

    return selected_stuff

stuff = get_selected_items_list(stuffdict)
print(stuff)

totarea = sum([stuffdict[item][0] for item in stuff])
totvalue = sum([stuffdict[item][1] for item in stuff])
print(totarea)
print(totvalue)
