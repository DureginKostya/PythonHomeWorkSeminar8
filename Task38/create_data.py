# def input_surname():
#     return input('Фамилию: ')

# def input_firstname():
#     return input('Имя: ')

# def input_patronymic():
#     return input('Отчество: ')

# def input_num_phone():
#     return input('Номер телефона: ')

def input_path_file(msg):
    path_file = input(msg)
    expansion = path_file[len(path_file) - 4:]
    while expansion != '.txt':
        print('Файл должен быть с расширением ".txt"')
        path_file = input(msg)
        expansion = path_file[len(path_file) - 4:]
    return path_file