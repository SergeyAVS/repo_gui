hw_list = ['Зимний месяц', 'Весенний месяц', 'Летний месяц', 'Осенний месяц']
hw_dict = {1 : 'Зимний месяц', 2 : 'Весенний месяц', 3 : 'Летний месяц', 4 : 'Осенний месяц'}
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
        print(hw_dict.get(1))
        print(hw_list[0])
elif month == 3 or month == 4 or month ==5:
    print(hw_dict.get(2))
    print(hw_list[1])
elif month == 6 or month == 7 or month == 8:
    print(hw_dict.get(3))
    print(hw_list[2])

elif month == 9 or month == 10 or month == 11:
    print(hw_dict.get(4))
    print(hw_list[3])
else:
        print("Такого месяца не существует")