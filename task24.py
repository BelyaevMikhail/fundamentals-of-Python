# с 10 буквами как сделать не знаю!
my_str = str(input('Введите несколько слов разделённых пробелами: '))
my_list = my_str.split()
print(my_list)

for ind, el in enumerate(my_list):
    print(ind, el)
