my_list = list(input('Какой цвет вам нравится?: '))
print(my_list)
my_cop = my_list.copy()
i = 0
i2 = 1
long = len(my_list)
while i < long - 1:
    my_list[i] = my_cop[i2]
    my_list[i2] = my_cop[i]
    i = i + 2
    i2 = i2 + 2
print(my_list)
