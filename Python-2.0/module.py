import random # random - случайность.

# Основные функции

# n = random.randint(1, 6) 
# print(n)

# n = random.random() # 0 до 1
# print(n)

# n = random.uniform(1.2, 10.5) # float - дробное число
# print(n)

# colors = ["красный", "синий", "зелёный"]
# n = random.choice(colors)
# print(n)

# print("Old:", colors)

# random.shuffle(colors)
#  return - давал значение. Но shuffle - не дает/ NONE.

# print("Shuffled Colors:", colors) 

# ЗАДАНИЕ 2:
# Компьютер загадывает число от 1 до 20. 
# Игрок вводит догадки. 
# Программа говорит «больше» или «меньше», пока игрок не угадает. 
# В конце выводит число попыток.

n = random.randint(1, 20)

# For - используется когда мы знаем сколько раз повторяться
# While - используется когда мы НЕ знаем сколько раз повторяться

# как работает счетчик? 
# 1. Создать переменную, которая будет увеличиваться. Обычно равняется 0.
# 2. Используем переменную, мы добавляем + 1

count = 0

while True:
    a = int(input("Угадайте число: "))
    count += 1 # count = count + 1
    
    if a < n:
        print("Больше")
    elif a > n:
        print("Меньше")
    else:
        print(f"Вы нашли это число - {n}. За {count} попыток!")
        break