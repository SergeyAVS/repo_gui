with open('test_txt_3.txt', 'r') as f_obj_3:
    sal = []
    poor = []
    my_list = f_obj_3.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')