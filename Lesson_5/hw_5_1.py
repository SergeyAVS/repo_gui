# fname = input('Имя файла: ')
f_obj = open('test_txt.txt', 'w')

line = input('Введите текст:\n')
while line:
    f_obj.writelines(line)
    line = input('Введите текст:\n')
    if not line:
        break

f_obj.close()
f_obj = open('test_txt.txt', 'r')
content = f_obj.readlines()
print(content)
f_obj.close()

