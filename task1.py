print("Программа перевода времени")
duration = int(input("Введите время в секундах: "))

day = 86400
hour = 3600
minute = 60

if duration < minute:
    print(duration, "сек")

elif duration >= minute and duration < hour:
    user_minute = duration // minute
    user_second = duration % minute
    print(user_minute, "мин", user_second, "сек")

elif duration >= hour and duration < day:
    user_hour = duration // hour
    duration = duration % hour
    user_minute = duration // minute
    user_second = duration % minute
    print(user_hour, "час", user_minute, "мин", user_second, "сек")

elif duration >= day:
    user_day = duration // day
    duration = duration % day
    user_hour = duration // hour
    duration = duration % hour
    user_minute = duration // minute
    user_second = duration % minute
    print(user_day, "дн", user_hour, "час", user_minute, "мин", user_second, "сек")