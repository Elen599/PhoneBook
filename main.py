from tkinter import*
from model import *
from tkinter import messagebox

# Функция вывода в отдельном окошке результата поиска 
def resul_find(text):
    messagebox.showinfo('Найдено:', text)

# Функция сохранения  
def save_contacts():
    data = list(list_box.get(0, END))
    for i, el in enumerate(data):
        x = el.find('.')
        data[i] = el[(x+2):].lstrip()
    write_file(data)

# Функция добавления контакта в справочник (с автосохранением)
def add_line():
    global spisok
    box = (str(len(spisok)+1) + '.    ' +
           contact.get() + '; ' +
           number.get() + '; ' +
           comment.get())
    contact.delete(0, END)
    number.delete(0, END)
    comment.delete(0, END)
    list_box.insert(END, box)
    save_contacts()

# Функция удаления контакта из справочника
def delete_line():
    list_box.delete(list_box.curselection())
    save_contacts()
    global spisok
    global spisok_box
    spisok = read_file()
    spisok_box = Variable(value=spisok)
    list_box.config(listvariable=spisok_box)

# Функция изменения контакта
def change_line():
    line = list_box.get(list_box.curselection()).split('; ')
    list_box.delete(list_box.curselection())
    temp = line[0]
    line[0] = temp[(temp.find('.'))+1:].lstrip()
    contact.delete(0, END)
    contact.insert(0, line[0])
    number.delete(0, END)
    number.insert(0, line[1])
    comment.delete(0, END)
    comment.insert(0, line[2])

# Функция поиска контакта (результат выводит в доп окошке)
def find_contact():
    res = ''
    global spisok
    spisok = read_file()
    for el in spisok:
        if find_entry.get().lower() in el.lower():
            res += el + '\n'
    resul_find(res)


window = Tk()
window.title('Телефонный справочник')
window.geometry('520x300+700+300')
window.resizable(False, False)
window.iconbitmap("telephone.ico")
spisok = read_file()
spisok_box = Variable(value=spisok)

head_label = Label(text='№   Имя контакта   Номер телефона   Комментарий          ')
head_label.pack()
list_frame = Frame()
list_frame.pack()
list_box = Listbox(list_frame, listvariable=spisok_box, height = 10, width = 50)
scrollbar = Scrollbar(list_frame, orient="vertical", command = list_box.yview)
list_box.config(yscrollcommand = scrollbar.set)
scrollbar.pack(side = RIGHT, fill = Y)
list_box.pack()


clik_frame = Frame()
clik_frame.pack()

contact_label = Label(clik_frame, text='Имя контакта')
contact_label.grid(column=1, row=0)
numbers_label = Label(clik_frame, text='Номер телефона')
numbers_label.grid(column=2, row=0)
change_label = Label(clik_frame, text='Комментарий')
change_label.grid(column=3, row=0)

contact = Entry(clik_frame)
contact.grid(column=1, row=1, padx=10)
number = Entry(clik_frame)
number.grid(column=2, row=1, padx=10)
comment = Entry(clik_frame)
comment.grid(column=3, row=1, padx=10)

add_btn = Button(clik_frame, text='Добавить', command=add_line)
add_btn.grid(column=0, row=2, sticky=NSEW, padx=5, pady=3)
delete_btn = Button(clik_frame, text='Удалить', command=delete_line)
delete_btn.grid(column=1, row=2,sticky=NSEW, padx=5, pady=3)
change_btn = Button(clik_frame, text='Изменить', command=change_line)
change_btn.grid(column=2, row=2, sticky=NSEW, padx=5, pady=3)
find_btn = Button(clik_frame, text='Поиск', command=find_contact)
find_btn.grid(column=3, row=2, sticky=NSEW, padx=5, pady=3)

find_label = Label(clik_frame, text='Введите имя для поиска:')
find_label.grid(column=1, row=4, columnspan=2, sticky='e')
find_entry = Entry(clik_frame)
find_entry.grid(column=3, row=4)

window.mainloop()