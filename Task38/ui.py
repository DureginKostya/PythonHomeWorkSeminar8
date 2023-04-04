from processing_writing import *
def hint():
    print('Какое действие желаете выполнить:' + '\n' + 
        '\t' + '1) импортировать данные в телефонный справочник (введите "i")' + '\n' +
        '\t' + '2) просмотр телефонного справочника (введите "v")' + '\n' +
        '\t' + '3) поиск (введите "f")' + '\n' +
        '\t' + '4) добавить запись в телефонный справочник (введите "a")' + '\n' +
        '\t' + '5) экспортировать данные из телефонного справочника (введите "o")' + '\n' +
        '\t' + '6) выйти из телефонного справочника (введите "e")')
    print()
    return input('Введите действие: ').lower()

def hint_find():
    print('Выберите тип поиска:' + '\n' + 
        '\t' + '1) по фамилии (введите "s")' + '\n' +
        '\t' + '2) по имени (введите "n")' + '\n' +
        '\t' + '3) по номеру телефона (введите "t")' + '\n' +
        '\t' + '4) завершить поиск (введите "e")')
    print()   
    return input('Искать по: ').lower()

def interface():
    print('<<< Телефонный справочник >>>')
    key = hint()
    while key != 'e':        
        if key == 'i':
            import_writing()
            input('Для продолжения, нажмите "Enter"')
        elif key == 'v':
            viewer_writing()
            input('Для продолжения, нажмите "Enter"')
        elif key == 'f':
            key_f = hint_find()
            while key_f != 'e':
                if key_f in ('s', 'n', 't'):
                    result_search = search_writing(key_f)
                    if len(result_search) != 0:
                        print(*result_search)
                    else:
                        print('Ничего не найдено!!!', end='\n\n')
                    input('Для продолжения, нажмите "Enter"')
                else:
                    print('Введено недопустимое значение', end='\n\n')
                key_f = hint_find()
            input('Для продолжения, нажмите "Enter"')
        elif key == 'a':
            add_writing(True)
            input('Для продолжения, нажмите "Enter"')
        elif key == 'o':
            export_writing()
            input('Для продолжения, нажмите "Enter"')
        else:
            print('Введено недопустимое значение', end='\n\n')
        key = hint()
    print('До свидания!!!')

interface()