print("Список, состоящий из кубов нечётных чисел")

def sum_of_number(number: int):
    res = 0
    while number > 0:
        res += number % 10
        number //= 10
    return res

list_of_odd = range(1, 1000, 2)

sum_with_17: int = 0
sum_without_17: int = 0

for elem in list_of_odd:
    cube = elem ** 3
    cube_with_17 = cube + 17
    if sum_of_number(cube) % 7 == 0:
        sum_without_17 += cube
    if sum_of_number(cube_with_17) % 7 == 0:
        sum_with_17 += cube_with_17

print("Сумма чисел без 17:", sum_without_17)
print("Сумма чисел c 17:", sum_with_17)