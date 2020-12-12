'''
Дубль 2
'''
def list_name():
    name_var = input('Введите ваше имя: ')
    last_name = input('Введите вашу фамилию: ')
    age = input('Сколько вам лет: ')
    cyti_m = input('В каком городе вы живёте: ')
    email_m = input('Введите вашу электронную почту: ')
    phone_m = input('Введите ваш номер телефона: ')
    return name_var, last_name, age, cyti_m, email_m, phone_m
a = list_name()
print(a)