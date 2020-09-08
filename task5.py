revenue = int(input('Введите значение выручки фирмы'))
cost = int(input('Введите значение издержек фирмы'))
gain = revenue - cost
if gain > 0:
    print('Фирма работает с прибылью! Доход составляет ', + gain,)
    print('Рентабельность работы фирмы:', + gain / revenue)
    digit = int(input('Введте количество сотрудников фирмы'))
    print('Прибиль фирмы на одного сотрудника: ', + gain / digit)
elif gain == 0:
    print('Фирма не приносит дохода')
else:
    print('Фирма работает в убыток')
