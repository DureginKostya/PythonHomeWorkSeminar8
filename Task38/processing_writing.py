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
    except:
        print('Указанный файл не найден')

# def export_writing():
#     return

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

# def add_writing():
#     return

# def search_writing():
#     return

# def change_writing():
#     return

# def del_writing():
#     return