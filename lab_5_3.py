
'''Вариант 1'''


'Строчка с данными: id, фамилия, электронная почта, дата регистрации и сайт'


import re


with open('task3') as file:
    for line in file:
        # отделить ДВА SURNAME:
        line = re.sub(r'([A-Z][a-z]+)([A-Z][a-z]+)',
                      r'\1 \2', line)

        # отделить НАЧАЛО SURNAME от всего остального:
        line = re.sub(r'([^(a-z)]*)([A-Z][a-z]+)', r'\1 \2', line)

        # отделить КОНЕЦ SURNAME от всего остального:
        line = re.sub(r'([A-Z][a-z]+)(\d+)', r'\1 \2', line)

        # отделить НАЧАЛО SURNAME от НАЧАЛА EMAIL
        line = re.sub(r'([A-Z][a-z0-9]*)([a-z0-9]+@[a-z0-9]+)',
                      r'\1 \2', line)


        # отделить НАЧАЛО DATE_REGISTRATION от всего остального:
        line = re.sub(r'(\d{1,10})(202)', r'\1 \2', line)

        # отделить КОНЕЦ DATE_REGISTRATION от всего остального:
        line = re.sub(r'(-\d{2}-\d{2})(.)', r'\1 \2', line)


        # отделить НАЧАЛО EMAIL от всего остального:
        line = re.sub(r'(\d{1,10})([a-z]{1,10})', r'\1 \2', line)

        # отделить КОНЕЦ EMAIL от всего остального:
        line = re.sub(r'(\.org)([^/])', r'\1 \2', line)
        line = re.sub(r'(\.net)([^/])', r'\1 \2', line)
        line = re.sub(r'(\.biz)([^/])', r'\1 \2', line)
        line = re.sub(r'(\.com)([^/])', r'\1 \2', line)
        line = re.sub(r'(\.info)([^/])', r'\1 \2', line)


        # отделить НАЧАЛО WEBSITE от всего остального:
        line = re.sub(r'(.)(http)', r'\1 \2', line)

        # отделить КОНЕЦ WEBSITE от всего остального:
        line = re.sub(r'org/', r'org/ ', line)
        line = re.sub(r'net/', r'net/ ', line)
        line = re.sub(r'biz/', r'biz/ ', line)
        line = re.sub(r'com/', r'com/ ', line)
        line = re.sub(r'info/', r'info/ ', line)

        #print(line) # разделенные фрагменты кроме id


# НАЙТИ id_draft:
id_draft = re.findall(r'\s\d+\s', line)
# НАЙТИ SURNAME:
surname = re.findall(r'\s[A-Z][a-z]+\s|\s[A-Z][a-z]+[^\s]', line)
# НАЙТИ EMAIL:
email = re.findall(r'[a-z0-9]+@[a-z0-9]+', line)
# НАЙТИ DATE_REGISTRATION:
date_registration = re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', line)
# НАЙТИ WEBSITE:
website = re.findall(r'[a-z]{4,5}://\S+', line)


id_draft = [int(x) for x in id_draft]

id = []
id.append(id_draft[0]) # т.к не войдет в range

for i in range(1, len(id_draft)-1):
    k = id_draft[i-1]
    x = id_draft[i]
    y = id_draft[i+1]

    id.append(x)

    # разделить ДВА ДВУХЗНАЧНЫХ числа
    if len(str(x)) == 4 and len(str(k)) == 2:
        id.remove(x)
        a = str(x)[:2]
        b = str(x)[2:]

        id.append(a)
        id.append(b)

    # разделить ДВА ТРЕХЗНАЧНЫХ числа
    if ((len(str(x)) == 6 and len(str(y)) == 3) or
            (len(str(x)) == 6 and len(str(k)) == 3)):
        id.remove(x)
        a = str(x)[:3]
        b = str(x)[3:]

        id.append(a)
        id.append(b)

    # разделить ДВА ЧЕТЫРЕХЗНАЧНЫХ числа
    if ((len(str(x)) == 8 and len(str(y)) == 4) or
            (len(str(x)) == 8 and len(str(k)) == 4)):
        id.remove(x)
        a = str(x)[:4]
        b = str(x)[4:]

        id.append(a)
        id.append(b)

    # разделить ЧЕТЫРЕХЗНАЧНОЕ и ОДНОЗНАЧНОЕ числа
    if len(str(x)) == 5:
        id.remove(x)
        a = str(x)[:4]
        b = str(x)[4:]

        id.append(a)
        id.append(b)

id = [int(x) for x in id]

id.append(id_draft[-1]) # т.к не вошел в range


'''
print(len(id))
print(len(surname))
print(len(email))
print(len(date_registration))
print(len(website))
'''


if __name__ == '__main__':
    print('id фамилия электронная_почта дата_регистрации сайт')
    for i in range(len(id)):
        print(id[i], surname[i], email[i], date_registration[i], website[i])

