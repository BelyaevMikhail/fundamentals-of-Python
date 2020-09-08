# создание списка и эксперементы с ним
my_list = list('список')
my_list.insert(2, 3.14)
my_list.insert(5, 5)
my_list.remove('п')
my_list.pop(2)
my_list.pop(2)
n_1 = complex(5, 6)
second_list = [1, 2]
tup = (5, 6)
plenty = frozenset('список')
my_list.insert(0, plenty)
my_list.insert(-3, tup)
my_list.insert(-1, second_list)
my_list.insert(2, n_1)
my_list.append(None)
my_list.reverse()
print(my_list)
# Определение типов в списке
for el in my_list:
    print(type(el))
