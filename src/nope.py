import random
from tkinter import *
import json
import os

"""
RhodoLab NopeSystem.
GNU GPL 3.0

All rights reserved
"""

lette1 = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
          'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
          'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
          'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21,
          'w': 22, 'x': 23, 'y': 24, 'z': 25, 'X': 28}

lette2 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
          5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
          10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o',
          15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v',
          22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: 'a', 27: 'b', 28: 'X', 29: 'X', 30: ' '}

lette3 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
          5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
          10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o',
          15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v',
          22: 'w', 23: 'x', 24: 'y', 25: 'z'}


def key():
    inkey = inp_key.get()
    linkey = list(inkey)

    key_win = Tk()
    key_win.title("Your key")
    key_win.geometry("500x300")

    out = []
    cond = "[block:added]"

    for i in range(len(linkey)):
        lcenkey = lette1[linkey[i]] + 2

        out.append(lette2[lcenkey])
        out.append(str(random.randint(0, 16)))

    st = ''
    key_w = st.join(out)
    key_lb = Label(key_win, text=key_w, font="Arial 16")
    key_lb.pack(anchor=NW)

    if inkey == "":
        labX = Label(key_win, text="X", font="Arial 16", foreground="red")
        labX.pack(anchor=NW)
    # with open('pass.txt', 'a') as f:
    #     f.write("[block:added:]\n")
    #     f.write(f"{key_w}\n")

    # cenkey = lette1[inkey] + 2
    # print(lette2[cenkey])

def virtpes():
    virt = Toplevel()
    virt.geometry("1080x720")
    virt.title("Встроеная песочница RhodoBX")

    lbv = Label(virt, text="Создание", font="Arial 10")
    #lbv.grid(row=0, column=0, sticky=N)

    lbb = Label(virt, text="Сначала выберите Процессор и материнскую плату", font="Arial 16")
    #lbb.grid(row=1, column=0, sticky=N)

    procbtn = Button(virt, text="Процессор", image=ph4, width=100, height=100)
    procbtn.grid(row=2, column=0)

    matbtn = Button(virt, text="Материнская плата", image=ph5, width=100, height=100)
    matbtn.grid(row=2, column=1)

    virt.mainloop()

def dbcr():
    dbp = Toplevel()
    dbp.geometry("720x480")
    dbp.title("Создание Базы данных с ключами")

    lbtr = Label(dbp, text="Введите название своей бд", font="Arial 12")
    lbtr.grid(row=0, column=0, sticky=N)

    vvodim = Entry(dbp, font="Arial 16")
    vvodim.grid(row=0, column=1, sticky=N)

    ustnaz = Button(dbp, text="Установка")
    ustnaz.grid(row=0, column=2, sticky=N)
   
    dbp.mainloop()

def sprav():
    sprwin = Tk()
    sprwin.title("Справка и информация")
    sprwin.geometry("480x480")

def avirus():
    pass

def projkey():
    ch = str(input("Выберите что хотите сделать: [1]-Создать вБД [2]-Открыть вБД [3]-Удалить вБД: "))
    if ch == '1':
        print("Создание виртуальной базы данных, пожалуйста введите название своей БД")
        crdb = str(input("dbname> "))
        print("Теперь выберите объем вмещаемых шифров [0..256..] (вы можете выбрать сколько влезет в ваш компьютер)")
        vsh = int(input("cap>"))
        with open(f"{crdb}.json", "w") as dbf:
            s = '{'
            c = '}'
            dbf.write(f'{s}\n\t"name": "{crdb}",\n\t"capac": "{vsh}"\n{c}')
    if ch == '2':
        opf = str(input("Введите название открываемого вБД: "))
        with open(f"{opf}.json", "r") as off:
            op_data = json.load(off)

        print(f"\nНазвание вБД:               {op_data["name"]}")
        print(f"Кол-во вмещаемых шифров:    {op_data["capac"]}\n")

    if ch == '3':
        delf = str(input("Введите путь к удаляемому файл: "))
        os.remove(delf)

def hash(inhash):
    inhash

# Графический интерфейс пользователя

root = Tk()
root.geometry("720x480")
root.title("RhodoLab NopeSystem")

ph = PhotoImage(file="key.png")
ph1 = PhotoImage(file="spr.png")
ph2 = PhotoImage(file="papka.png")
ph3 = PhotoImage(file="pesok.png")
ph4 = PhotoImage(file="processor.png")
ph5 = PhotoImage(file="matplat.png")
ph6 = PhotoImage(file="antivirus.png")

kcan = Canvas(root, width=400, height=200, bg="white")
kfr = Frame(root, width=300, height=150, bg='blue')
# kfr.pack(anchor=NW)

crtbtn = Button(root, text="key", image=ph, width=100, height=100, font="Arial", command=key)
# crtbtn.pack(anchor=NW, padx=5, pady=5)
crtbtn.grid(row=0, column=0, sticky=N)

inp_key = Entry(root, font="Arial 16")
# inp_key.pack(anchor=N, pady=0)
inp_key.grid(row=0, column=1, sticky=N)

papbtn = Button(root, image=ph2, width=100, height=100, command=dbcr)
papbtn.grid(row=0, column=2)

virpbtn = Button(root, image=ph3, width=100, height=100, command=virtpes)
virpbtn.grid(row=1, column=1)

sprbtn = Button(root, text="key", image=ph1, width=100, height=100, font="Arial", command=sprav)
# sprbtn.pack(anchor=SW)
sprbtn.grid(row=1, column=0, sticky=N)

avbtn = Button(root, text="avirus", image=ph6, width=100, height=100, font="Arial", command=avirus)
# avbtn.pack(anchor=SW)
avbtn.grid(row=1, column=2, sticky=N)

if __name__ == '__main__':
    root.mainloop()

# Бэкап консольной версии 

# print("""
# RhodoLab. NopeSystem Pro. 
# - Local Cybersecurity System
# RhodoLab Corp. Copyright.
#       
# Software was distributed with GNU GPL 3.0
# """)
# 
# print("mode seted - default\n")



# while True:
#     # Смена режима
#     law = 0
#     if law == 0:
#         user = str(input("[User *(I)]- "))
#     if law == 1:
#         user = str(input("[User *(J)]- "))
#     if user == "secret":
#         law = 1
#         user = str(input("[User *(J)]- "))
#     if user == "default":
#         law = 0
#         user = str(input("[User *(I)]- "))
# 
#     # Процесс
# 
#     if user == "rhodobx":
#         print("RhodoBX - The local cybersec sandbox")
#         print("type helpbx to get help documentation\n")
#         bxr = str(input("RhodoBX-input ]= "))
#         while bxr != "exit":
#             bxr = str(input("RhodoBX-input ]= "))
# 
#     # Процесс.Справки
#     if user == "help":
#         print("\nkey     - одинарное шифрование данных")
#         print("projkey - создание виртуальной базы данных")
#         print("titles  - титры/авторы")
#         print("nope    - информация о программе")
#         print("rhodobx - встроенная песочница ПК и серверов")
#         print("rules   - гайд на шифрование")
#         print("exit    - выход\n")
# 
#     if user == "rules":
#         print("\nЧтобы зашифровать текст с помощью")
#         print("протокола KDSA вам нужно написать команду key и ввести свои данные.")
#         print("""Чтобы создать некий пробел между строками \nпишите X(англ.) чтобы разделить строку\n""")
# 
#     if user == "nope":
#         print("\nNopeSystem - это цифровая экосистема локальной кибербезопасности а также тестирования,")
#         print("созданная компанией RhodoLab под лицензией GNU GPL 3.0. Данное ПО является бесплатным и открытым")
#         print("Но защищено авторскими правами и торговой маркой RhodoLab.\n")
#     
#     # Процесс.Шифрование/Хеширование
#     if user == "key":
#         key(str(input("Введите данные: ")))
# 
#     if user == "projkey":
#         projkey()
# 
#     #Процесс.Выход
#     if user == "exit":
#         break
# 
#     # Процесс.Безделушки
#     if user == "titles":
#         print("Автор - Кабардиков Имран (в интернете известен как imkablit или ImranKab)")
#         print("Разработчик - RhodoLab Инк.")