import random
import json
import os

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


def key(inkey):
    linkey = list(inkey)

    out = []
    cond = "[block:added]"

    for i in range(len(linkey)):
        lcenkey = lette1[linkey[i]] + 2

        out.append(lette2[lcenkey])
        out.append(str(random.randint(0, 16)))

    st = ''
    key_w = st.join(out)
    print(f"Ваш шифр: {key_w}")
    # with open('pass.txt', 'a') as f:
    #     f.write("[block:added:]\n")
    #     f.write(f"{key_w}\n")

    # cenkey = lette1[inkey] + 2
    # print(lette2[cenkey])

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

print("""
RhodoLab. NopeSystem Pro. 
- Local Cybersecurity System
RhodoLab Corp. Copyright.
      
Software was distributed with GNU GPL 3.0
""")

print("mode seted - default\n")

while True:
    # Смена режима
    law = 0
    if law == 0:
        user = str(input("[User *(I)]- "))
    if law == 1:
        user = str(input("[User *(J)]- "))
    if user == "secret":
        law = 1
        user = str(input("[User *(J)]- "))
    if user == "default":
        law = 0
        user = str(input("[User *(I)]- "))

    # Процесс

    if user == "rhodobx":
        print("RhodoBX - The local cybersec sandbox")
        print("type helpbx to get help documentation\n")
        bxr = str(input("RhodoBX-input ]= "))
        while bxr != "exit":
            bxr = str(input("RhodoBX-input ]= "))

    # Процесс.Справки
    if user == "help":
        print("\nkey - одинарное шифрование данных")
        print("projkey - создание виртуальной базы данных")
        print("titles - титры/авторы")
        print("rules - гайд на шифрование")
        print("exit - выход\n")

    if user == "rules":
        print("\nЧтобы зашифровать текст с помощью")
        print("протокола KDSA вам нужно написать команду key и ввести свои данные.")
        print("""Чтобы создать некий пробел между строками \nпишите X(англ.) чтобы разделить строку\n""")

    if user == "nope":
        print("\nNopeSystem - это цифровая экосистема локальной кибербезопасности а также тестирования,")
        print("созданная компанией RhodoLab под лицензией GNU GPL 3.0. Данное ПО является бесплатным и открытым")
        print("Но защищено авторскими правами и торговой маркой RhodoLab.\n")
    
    # Процесс.Шифрование/Хеширование
    if user == "key":
        key(str(input("Введите данные: ")))

    if user == "projkey":
        projkey()

    #Процесс.Выход
    if user == "exit":
        break

    # Процесс.Безделушки
    if user == "titles":
        print("Автор - Кабардиков Имран (в интернете известен как imkablit)")
        print("Разработчик - RhodoLab Инк.")
