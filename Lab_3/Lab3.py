def read_file(file_path, type_of_read = 0):
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:

            if type_of_read == 0:

                data = file.read()
                print(data)

            else:

                for id, line in enumerate(file):
                    print(id+1, line, end='')
    except FileNotFoundError:
        print("Файл не обнаружен")
    except:
        print("Непредвиденная ошибка")



def write_file(file_path, type_of_write = 0):

    if type_of_write == 0:
        enter_key = 'w' # перезапись файла с предшествующей отчисткой или создание нового файла если тот не существовал
    else:
        enter_key = 'a' # дозапись файла или создание нового файла если тот не существовал

    with open(file_path, enter_key, encoding = 'utf-8') as file:

        data = input("Введите данные: ") + '\n'
        file.write(data)



if __name__ == '__main__':
    
    read_file('example.txt', 0) # чтение всего файла сразу 
    print('----------------------------')
    read_file('example.txt', 1) # построчное чтение

    print('\n=========================================')

    write_file('user_input.txt', 0) # запись текста в новый файл
    read_file('user_input.txt', 0) # чтение всего файла сразу 
    print('----------------------------')
    write_file('user_input.txt', 1) # дозапись текста в имеюзщийся файл
    read_file('user_input.txt', 0) # чтение всего файла сразу 