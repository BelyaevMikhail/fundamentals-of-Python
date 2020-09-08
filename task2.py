seconds = int(input('Введите количество секунд'))

hour = seconds // 3600
minute = (seconds // 60) % 60
second = seconds % 60

if hour < 10:
    hour = str('0' + str(hour))
else:
    if hour > 24:
        day = (hour // 24)
        hour = hour - day * 24
        if hour < 10:
            hour = str(str(day) + ' суток и 0' + str(hour))
        else:
            hour = str(str(day) + ' суток и ' + str(hour))
    else:
        hour = str(hour)

if minute < 10:
    minute = str('0' + str(minute))
else:
    minute = str(minute)

if second < 10:
    second = str('0' + str(second))
else:
    second = str(second)

print(str(hour) + ':' + str(minute) + ':' + str(second))
