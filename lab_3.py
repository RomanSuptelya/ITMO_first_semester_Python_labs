
'''Вариант 1'''


'Каждый блок имеет две цифры и три буквы в случайном порядке.'


from tkinter import *
import string
import random


def mixed_parol(mix_0=0, mix_1=0, mix_2=0):
    for i in range(3): # создаем три блока случайных знаков
        random_letters_i = [random.choice(string.ascii_uppercase)
                            for i in range(3)] # 3 случайных буквы
        random_digits_i = [random.choice(string.digits)
                           for j in range(2)] # 2 случайные цифры

        # добавим в массив all 3 буквы и 2 цифры
        all_i = []
        for j in range(3):
            all_i.append(random_letters_i[j])
        for k in range(2):
            all_i.append(random_digits_i[k])

        # перемешаем массив all
        mix_i = ''
        random.shuffle(all_i)
        for n in range(5):
            mix_i = mix_i + all_i[n]

        # три разных блока случайных символов
        if i == 0:
            mix_0 = mix_i
        elif i == 1:
            mix_1 = mix_i
        elif i == 2:
            mix_2 = mix_i

    # f'{mix_0}-{mix_1}-{mix_2}' - три блока случайных символов

    lbl_1 = Label(window, text=f'{mix_0}-{mix_1}-{mix_2}',
                  font=("Arial Bold", 50))  # создаем текстовую метку
    lbl_1.grid(column=0, row=2)  # размещаем текст в окне


def clicked(): # функция, которую нужно выполнить после нажатия на кнопку
    lbl.configure(text="Ваш пароль")
    mixed_parol() # выводит сгенерированный пароль


window = Tk()  # создаем корневой объект - окно; функция window = функция root
window.title("Приложение на Tkinter")  # устанавливаем заголовок окна
window.geometry("3000x2500")  # устанавливаем размеры окна


#Добавим изображение
canvas = Canvas(window, height=650, width=750)
img = PhotoImage(file = "/Users/romansuptelya/Downloads/"
                        "vlr8o8qg9boxmndg7a9uxyw39mnsj9e3 2.png")
image = canvas.create_image(0, 0, anchor='nw',image=img)
canvas.grid(row=2,column=1)

lbl = Label(window, text="Генератор паролей",
            font=("Arial Bold", 50))  # создаем текстовую метку
lbl.grid(column=0, row=0) # размещаем текст в окне

btn = Button(window, text="Создать пароль", command=clicked)  # создаем кнопку
btn.grid(column=1, row=0) # размещаем кнопку в окне

window.mainloop() # бесконечно открытое окно. Должно быть всегда внизу
