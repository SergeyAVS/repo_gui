rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('test_txt_4.txt', 'r') as f_obj_4:
    for i in f_obj_4:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('test_txt_4_new.txt', 'w') as f_obj_4_2:
    f_obj_4_2.writelines(new_file)