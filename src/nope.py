import random
import math
import json
import os
import sys
from nopeapi import nopedb

"""
RhodoLab NopeSystem.
GNU GPL 3.0

All rights reserved
"""

class Virus():
    def __init__(self):
        pass
    def crypt():
        pass

virus = Virus()

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

sym = {0: '$', 1: '#', 2: '&', 3: '@', 4: ':', 5: '%', 6: '*', 7: '?', 8: '!'}

edb = {'py': "Файл языка программирования Python", 'xlsx': "Файл таблицы Excel",
       'txt': "Стандартный текстовый файл", 'cpp': "Файл языка программирования C++",
       'html': "Файл браузерной веб-страницы", 'dll': "Файл динамической библиотеки Windows"}

def key(inkey):
    linkey = list(inkey)

    out = []
    cond = "[block:added]"

    for i in range(len(linkey)):
        lcenkey = lette1[linkey[i]] + 2

        out.append(lette2[lcenkey])
        out.append(str(sym[random.randint(0, 8)]))

    st = ''
    key_w = st.join(out)
    with open("nopecache", "a") as fcache:
        fcache.write(f"{key_w}\n")
    print(f"Ваш шифр: {key_w}")

def avirus():
    podoz_str = ['sudo rm -rf /', 'sudo rm -rf /\n', 'sudo rm -rf --no-preserve-root /',
             'sudo rm -rf /home', 'sudo rm -rf --no-preserve-root /home', 'sudo rm -rf --no-preserve-root /home\n']
    
    
    virus = str(input("Введите путь к файлу который подозреваете: "))

    try:
        with open(f"{virus}", "r") as virf:
            vir = virf.readlines()
    except FileNotFoundError:
        print("Извините, но в текущей дериктории такого файла не существует.")

    opas = 0
    try:
        for i in range(len(vir)):
            if vir[i] == podoz_str[0] or vir[i] == podoz_str[1] or vir[i] == podoz_str[2] or vir[i] == podoz_str[3]:
                print(f"Nope-AV обнаружил в {i+1} строке подозрительность: код уязвимости: __MALSCRIPT")
            # opas = opas + 1
            else:
                print(f"в {i+1} строке не найдено подозрительных вещей")
    except UnboundLocalError:
        print("__NO_FILE__")

    print("Сканирование прошло")
    print(f"Всего опасных строк: {opas}")
    # print(vir, "\n")
    # if opas == 1:
    #     vibor_u = str(input())

def protoarch(indat):
    lindat = indat.split()
    print(lindat)

def fastif(uslov, op, ravn, vivod):
    if op == '==':
        if uslov == ravn:
            print(vivod)
    if op == '!=':
        if uslov != ravn:
            print(vivod)

def createbx():
    input()

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
    finh = list(inhash)
    cfin = []
    for i in range(len(finh)):
        gfinh = lette1[finh[i]]
        cfin.append(str(gfinh))

    st = ''
    outc = st.join(cfin)
    ioutc = int(outc)
    # if len(list(str(ioutc))) < 16:
    #     ioutc = ioutc * 1
    print(len(str(ioutc)))
    # if len(str(int(ioutc))) < 8:
    #     ioutc = ioutc * 131072
    # if len(str(int(ioutc))) < 16:
    #     ioutc = ioutc * 16384
    if len(str(int(ioutc))) < 16:
        i = 1
        while len(str(int(ioutc))) < 16:
            ioutc = ioutc * i
            i = i + 1
    elif len(str(int(ioutc))) > 16:
        while len(str(int(ioutc))) > 16:
            ioutc = ioutc / i 
            i = i + 4

    print(len(str(int(ioutc))))
    print(int(ioutc))
    print(cfin)

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
            if bxr == "create":
                createbx()
            bxr = str(input("RhodoBX-input ]= "))

    # Процесс.Справки
    if user == "help":
        print("\nkey     - одинарное шифрование данных")
        print("projkey - создание виртуальной базы данных")
        print("titles  - титры/авторы")
        print("nope    - информация о программе")
        print("rhodobx - встроенная песочница ПК и серверов")
        print("rules   - гайд на шифрование")
        print("exit    - выход\n")

    if user == "rules":
        print("\nЧтобы зашифровать текст с помощью")
        print("алгоритма JAT вам нужно написать команду key и ввести свои данные.")
        print("""Чтобы создать некий пробел между строками \nпишите X(англ.) чтобы разделить строку\n""")

    if user == "nope":
        print("\nNopeSystem - это цифровая экосистема локальной кибербезопасности а также тестирования,")
        print("созданная компанией RhodoLab под лицензией GNU GPL 3.0. Данное ПО является бесплатным и открытым")
        print("Но защищено авторскими правами и торговой маркой RhodoLab.\n")
    
    # Процесс.Манипуляции_с_файлами
    if user == "file":
        print("Выберите проф-манипуляции с файлами:")
        print("[1]-удалить все символы и слова по параметрам")
        print("[2]-узнать назначение(расширение) файла")
        fus = ""
        while fus != "exit":
            fus = str(input("Input the choose: "))
            if fus == "2":
                inpf = str(input("Введите полное название файла: "))
                # with open(f"{inpf}", "r") as f:
                #     pass
                sinpf = inpf.split('.')
                ext = sinpf[1]
                print(sinpf)
                print(edb[ext])

    if user == "archer":
        protoarch(str(input("Input the Indata: ")))

    # Процесс.Шифрование/Хеширование
    if user == "key":
        key(str(input("Введите данные: ")))

    if user == "projkey":
        projkey()

    if user == "hash":
        print("Хеширование данных с помощью RHM16")
        hash(str(input("Введите входные данные: ")))

    # Процесс.Антивирус 
    if user == "nope-av":
        avirus()

    # Процесс.Система_аккаунтов (с использованием хеширования RHM16)
    if user == "account":
        pass

    #Процесс.Выход
    if user == "exit":
        os.remove("nopecache")
        break

    if user == "clear":
        print('\r')

    if user == "debug":
        print(sys.getsizeof(user))
        print(os.path.getsize("nopecache"))

    # Процесс.Безделушки
    if user == "random":
        print("Алгоритм рандомизации случайных чисел в Nope")
        print("Полностью написанный разработчиками")

    if user == "titles":
        print("Автор - Кабардиков Имран (в интернете известен как imkablit или ImranKab)")
        print("Разработчик - RhodoLab Инк.")
