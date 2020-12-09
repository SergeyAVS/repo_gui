a = []
for i in range(int(input('Введите количество элементов в списке: '))):
    a.append(input('Введите элемент списка: '))
print(a) #Все элементы получаются строка, если перед input поставить int
# все элементы будут целыми числами
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))