print("Склонение слова «процент»")

percent = 0

while percent <= 100:
    remain = percent % 100
    if remain >= 20:
        remain %= 10
    if remain == 1:
        print(percent, "процент")
    elif 2 <= remain <= 4:
        print(percent, "процента")
    else:
        print(percent, "процентов")
    percent += 1