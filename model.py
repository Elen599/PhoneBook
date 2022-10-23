# Функция записи в переменную прочитанного файла .txt (в т.ч. порядкового номера)
def read_file():
    with open('contacts.txt', 'r', encoding='utf-8') as data:
        phone = data.read().split('\n')
    for i, el in enumerate(phone):
        phone[i] = str(i+1) + '.   ' + el
    return phone

# Функция ззаписи в .txt (с ограничением формирования пустой строки)
def write_file(data):
    with open('contacts.txt', 'w', encoding='utf-8') as file:
        for i, el in enumerate(data):
            if (i+1) == len(data):
                file.write(el)
            else:
                file.write(el + '\n')