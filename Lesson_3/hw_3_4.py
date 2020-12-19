'''
Дубль 2
'''
def my_fu (x, y):
    return 1 / x ** abs(y)


def myi_fu (a, d):
    z = 1
    for i in range(abs(d)):
        z = z * a
    return 1 / z
print (my_fu(2,-5))
print(myi_fu(2, -5))