s = float(input("Введите количество лет: "))

if s < 0:
    print("Ошибка: количество лет не может быть отрицательным.")
else:
    if s <= 2:
        h = s * 10.5
    else:
        h = 21 + (s - 2) * 4

    print("Эквивалентно", h, "годам")
