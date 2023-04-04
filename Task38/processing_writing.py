from create_data import *
def import_writing():
    imp_path = input_path_file('Укажите путь и имя импортируемого файла: ')
    path_phone_book = input_path_file('Укажите путь и имя файла для импортирования данных: ')
    try:
        with open(imp_path.strip(), 'r', encoding='utf-8') as imp_file:
            with open(path_phone_book.strip(), '+a', encoding='utf-8') as phone_book:
                for writing in imp_file:
                    phone_book.seek(0)
                    if writing not in phone_book:
                        phone_book.write(writing)
        print('Данные перенесены', end='\n\n')
    except:
        print('Указанный файл не найден')

def export_writing():
    exp_path = input_path_file('Укажите путь и имя файла для экспорта данных: ')
    path_phone_book = input_path_file('Укажите путь и имя экспортируемого файла: ')
    try:
        with open(path_phone_book.strip(), 'r', encoding='utf-8') as phone_book:
            with open(exp_path.strip(), '+a', encoding='utf-8') as exp_file:
                for writing in phone_book:
                    exp_file.seek(0)
                    if writing not in exp_file:
                        exp_file.write(writing)
        print('Данные перенесены', end='\n\n')
    except:
        print('Указанный файл не найден')

def viewer_writing():
    try:
        with open('my_phone_book.txt', 'r', encoding='utf-8') as phone_book:
            for writing in phone_book:
                writing = tuple(writing.split('!'))
                print(f'Фамилия: {writing[0]}')
                print(f'Имя: {writing[1]}')
                print(f'Отчество: {writing[2]}')
                print(f'Номер телефона: {writing[3]}')
    except:
        print('Телефонного справочника нет')

def add_writing(key_add):
    try:
        with open('my_phone_book.txt', 'a', encoding='utf-8') as phone_book:
            while key_add:
                print('Добавьте контакт:')
                surname = input_surname()
                firstname = input_firstname()
                patronymic = input_patronymic()
                num_phone = input_num_phone()
                while not num_phone.isdigit():
                    print('''Номер телефона должен содержать только цифры!!!
Введите повторно номер телефона''')
                    num_phone = input_num_phone()
                phone_book.write(f'{surname}!{firstname}!{patronymic}!{num_phone}\n')
                print('Контакт добавлен')
                sequel = input('Продолжить добавление контактов [yes/no]: ')
                while not sequel in ('yes', 'no'):
                    print('Введена неправильная команда, повторите ввод')
                    sequel = input('Продолжить: ')
                if sequel == 'no':
                    key_add = False
                print()
    except:
        print('Телефонного справочника нет')  

def search_writing(key_search):
    if key_search == 's':
        value = input_surname()
        ind = 0
    elif key_search == 'n':
        value = input_firstname()
        ind = 1
    else:
        value = input_num_phone()
        ind = 3
    print()
    print('Результат:')
    try:
        with open('my_phone_book.txt', 'r', encoding='utf-8') as phone_book:
            result = []
            for writing in phone_book:
                writing = writing.split('!')
                if value.strip().lower() == writing[ind].strip().lower():
                    phone_book.tell()
                    writing.append()
                    result.append(tuple(writing))
                    # print(f'Фамилия: {writing[0]}')
                    # print(f'Имя: {writing[1]}')
                    # print(f'Отчество: {writing[2]}')
                    # print(f'Номер телефона: {writing[3]}')
        return result
    except:
        print('Телефонного справочника нет')

# def change_writing():
#     return

# def del_writing():
#     return