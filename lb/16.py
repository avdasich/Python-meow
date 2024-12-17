import random

while 1:
    secret = random.randint(1, 10)
    a = 0
    print("Хорошо, я загадал число. Попробуй его отгадать")
    while 1:
        a += 1
        num = int(input("Введите число: "))
        print("Количество попыток: ", a)

        if num < secret:
            print("Ты близок,но число больше")
        elif num > secret:
            print("Теперь число меньше")
        else:
            print("Поздравляю! Вы угадали! Количество задействованных опыток:", a)
            break

    q = int(input("Хотите попробовать еще раз? Выберите 1 если да. Выберите 2 если нет: "))
    if q != 1:
        break
print("Спасибо за игру! Пока!")
