from sys import argv

name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')


# def simple_calc():
#     x = float(input('Введите количество отработанных часов : '))
#     y = float(input('Введите суммы оплаты труда за 1 час : '))
#     c = float(input('Укажите размер премии - '))
#     pay = x * y
#     return pay + c
# print(f'Размер заработной платы составил: {simple_calc() }')

