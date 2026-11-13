import random
import math
import json
import os
import sys

"""
RhodoLab NopeSystem 0.2.0
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
          'w': 22, 'x': 23, 'y': 24, 'z': 25, 'X': 1024}

lette2 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
          5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
          10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o',
          15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v',
          22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: 'a', 27: 'b', 1024: 'X', 1025: 'X', 1026: ' '}

symbols = {0: '$', 1: '#', 2: '&', 3: '@', 4: ':', 5: '%', 6: '*', 7: '?', 8: '!'}

extensions_db = {'py': "Файл языка программирования Python", 'xlsx': "Файл таблицы Excel",
       'txt': "Стандартный текстовый файл", 'cpp': "Файл языка программирования C++",
       'html': "Файл браузерной веб-страницы", 'dll': "Файл динамической библиотеки Windows",
       'lib': "Библиотека Linux", 'json': "Файл JSON (создан для структурирования данных)"}


def key(param_key):
    linkey = list(param_key)

    out_list = []
    try:
        for i in range(len(linkey)):
            lcenkey = lette1[linkey[i]] + 2

            out_list.append(lette2[lcenkey])
            out_list.append(str(symbols[random.randint(0, 8)]))
    except KeyError:
        print("Символа в заданной вами строке еще нет в списке стандартных для шифрования.")

    st = ''
    string_output = st.join(out_list)
    with open("nopecache", "a") as fcache:
        fcache.write(f"{string_output}\n")
    print(f"Ваш шифр: {string_output}")

def avirus():
    malvare_strings = ['sudo rm -rf /', 'sudo rm -rf /\n', 'sudo rm -rf --no-preserve-root /',
             'sudo rm -rf /home', 'sudo rm -rf --no-preserve-root /home', 'sudo rm -rf --no-preserve-root /home\n']
    
    
    virus = str(input("Введите путь к файлу который подозреваете: "))

    try:
        with open(f"{virus}", "r") as virus_file:
            virus_content = virus_file.readlines()
    except FileNotFoundError:
        print("Извините, но в текущей дериктории такого файла не существует.")

    danger = 0
    try:
        for i in range(len(virus_content)):
            if virus_content[i] in malvare_strings:
                print(f"Nope-AV обнаружил в {i+1} строке подозрительность: код уязвимости: __MALSCRIPT")
                opas = opas + 1
            else:
                print(f"в {i+1} строке не найдено подозрительных вещей")
    except UnboundLocalError:
        print("__NO_FILE__")
    print("Сканирование прошло")
    print(f"Всего опасных строк: {danger}")
    # print(vir, "\n")
    # if opas == 1:
    #     vibor_u = str(input())

def protoarch(in_data : str):
    splitted_in_data = in_data.split()
    print(splitted_in_data)

def fastif(statement, operation : str, ravn, output, output_else):
    if operation == '==':
        if statement == ravn:
            print(output)
        else:
            print(output_else)
    if operation == '!=':
        if statement != ravn:
            print(output)
        else:
            print(output_else)

def nopebx():
    print("NopeBX - поддержка NopeLinux - урезанный линукс для песочницы")
    choose_os = str(input("Выберите ОС для псевдо-песочницы"))
    if choose_os == "linux":
        direct = '$'
        while True:
            linux_command = str(input(f"server@nopelinux:~{direct} "))
            linux_command.split()
            if linux_command[0] == "cd":
                direct = linux_command[1]

def projkey():
    choose_type = str(input("Выберите что хотите сделать: [1]-Создать вБД [2]-Открыть вБД [3]-Удалить вБД: "))
    if choose_type == '1':
        print("Создание виртуальной базы данных, пожалуйста введите название своей БД")
        filepath = str(input("dbname> "))
        print("Теперь выберите объем вмещаемых шифров [0..256..] (вы можете выбрать сколько влезет в ваш компьютер)")
        input_capacity_line = int(input("cap>"))

        with open(f"{filepath}.json", "w") as db_file:
            db_file.write(f'{'{'}\n\t"name": "{filepath}",\n\t"capac": "{input_capacity_line}"\n{'}'}')

    if choose_type == '2':
        file_name = str(input("Введите название открываемого вБД: "))
        with open(f"{file_name}.json", "r") as file_for_open:
            db_data = json.load(file_for_open)
 
        print(f"\nНазвание вБД:             {db_data["name"]}")
        print(f"Кол-во вмещаемых шифров:    {db_data["capac"]}\n")

    if choose_type == '3':
        choosed_delete_file = str(input("Введите путь к удаляемому файл: "))
        os.remove(choosed_delete_file)

def hash(param_hash):
    listed_hash_in = list(param_hash)
    hash_list = []

    for i in range(len(listed_hash_in)):
        gfinh = lette1[listed_hash_in[i]]+1
        hash_list.append(str(gfinh))

    st = ''
    outc = st.join(hash_list)
    ready_hash = int(outc)

    if len(str(ready_hash)) < 64:
        i = 1
        while len(str(int(ready_hash))) < 64:
            ready_hash = ready_hash + i
            i = i * 2
    elif len(str(ready_hash)) > 64:
        while len(str(int(ready_hash))) > 64:
            ready_hash = ready_hash / i 
            i = i + 4

    print(len(str(int(ready_hash))))
    print(ready_hash)

if __name__ == '__main__':
    print("""
RhodoLab. NopeSystem Pro 0.2.1.1
(0.2.0.9 - 0.2.1.5 Refactoring)
- Local Cybersecurity System
RhodoLab Corp. Copyright.

Software was distributed with GNU GPL 3.0
    """)

    print("mode seted - default\n")

    law = 0
    while True:
        # Смена режима
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

        if user == "nopebx":
            nopebx()
            
        # Процесс.Справки
        if user == "help":
            print("\nkey       - одинарное шифрование данных")
            print("projkey   - создание виртуальной базы данных")
            print("titles    - титры/авторы")
            print("nope      - информация о программе")
            print("nopebx    - встроенная песочница ПК и серверов")
            print("rules     - гайд на шифрование")
            print("nopepanel - профессиональная панель")
            print("exit      - выход\n")

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
                    print(extensions_db[ext])

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

        if user == "nopepanel":
            print("Професиональная панель Nope")

        # Процесс.Безделушки
        if user == "random":
            print("Алгоритм рандомизации случайных чисел в Nope")
            print("Полностью написанный разработчиками")

        if user == "titles":
            print("Автор - Кабардиков Имран (в интернете известен как imkablit или ImranKab)")
            print("Разработчик - RhodoLab Инк.")