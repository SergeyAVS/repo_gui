def drob ():
    try:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        c = a / b
    except ZeroDivisionError:
        return 'ZeroDivisionError'
    except ValueError:
        return 'ValueError'
    return c
print(drob())