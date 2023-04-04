from processing_writing import *
def hint():
    print('Какое действие желаете выполнить:' + '\n' + 
        '\t' + '1) импортировать данные в телефонный справочник (введите "i")' + '\n' +
        '\t' + '2) просмотр телефонного справочника (введите "v")' + '\n' +
        '\t' + '3) поиск информации по фамилии (введите "f")' + '\n' +
        '\t' + '4) добавить запись в телефонный справочник (введите "a")' + '\n' +
        '\t' + '5) экспортировать данные из телефонного справочника (введите "u")' + '\n' +
        '\t' + '6) выйти из телефонного справочника (введите "e")')
    print()
    return input('Введите действие: ').lower()

def interface():
    print('<<< Телефонный справочник >>>')
    key = hint()
    while key != 'e':        
        if key == 'i':
            import_writing()   
        # elif action == 'v':
        #     viewing_directory()
        # elif action == 'f':
        #     surname = input('Введите фамилию: ')
        #     find_info_surname(surname)
        # elif action == 'i':
        #     file_import = input('Введите имя файла с расширением для импортирования данных: ')
        #     path_file_imp = input('Укажите путь к файлу: ')
        #     try:
        #         import_info(path_file_imp, file_import)
        #     except:
        #         print('По указанному пути нет нужного файла')
        # elif action == 'u':
        #     file_export = input('Введите имя файла с расширением для экспортирования данных: ')
        #     path_file_exp = input('Укажите путь к файлу: ')
        #     unload_info(path_file_exp, file_export)
        # elif key == 'e':
        #     print('До свидания!!!')
        else:
            print('Введено недопустимое значение')
        key = hint()
        if key == 'e':
            print('До свидания!!!')

interface()