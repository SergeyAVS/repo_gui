def summary():
    try:
        with open('test_text_5.txt', 'w+') as f_obj_5:
            line = input('Введите цифры через пробел \n')
            f_obj_5.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()