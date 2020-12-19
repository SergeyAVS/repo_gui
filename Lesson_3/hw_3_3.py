'''
Дубль 2
'''
def sum_max ():
    fi_1 = float(input('Введите первое число: '))
    fi_2 = float(input('Введите второе число: '))
    fi_3 = float(input('Введите третье число: '))
    fi_min = min(fi_1, fi_2, fi_3)
    sum_max_e = fi_1 + fi_2 + fi_3 - fi_min
    return sum_max_e, fi_min, fi_1, fi_2, fi_3
a = sum_max()
print('Сумма двух больших чисел равна:', a)