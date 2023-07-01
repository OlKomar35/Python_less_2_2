# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих 
# чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import math

summa = int(input('Сумма двух чисел ='))
mult = int(input('Произведение двух чисел ='))

if (summa ** 2 - 4 * mult) >= 0:
    num_first = (summa + math.sqrt(summa ** 2 - 4 * mult)) // 2
    num_second = (summa - math.sqrt(summa ** 2 - 4 * mult)) // 2

    if summa == num_first + num_second and mult == num_first * num_second:
        print(f'{num_first} {num_second}')
    else:
        print('не верное условие')
else:
    print('не верное условие')
