def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите, через пробел, любое количество чисел. Для выхода введите Q: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма всех чисел равна: {sum_res}')
    print(f'Программа завершена.')