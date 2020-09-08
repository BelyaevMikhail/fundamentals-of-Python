number = int(input('Введите целое положительное число'))
max_digit = number % 10
while number > 1:
    number = number // 10
    digit = number % 10
    if digit > max_digit:
        max_digit = digit
print('Самая большая цифра в вашем числе это: ' + str(max_digit))
