a = []

while 1:
    b = int(input("Введите рост или 0 для окончания: "))
    if b == 0:
        break
    if b < 0:
        print("Рост в - не учитывается.")
    else:
        a = a + [b]

if len(a) < 2:
    print("Некого сравнивать")
else:
    print("Самый высокий рост:", max(a))
    print("Самый низкий рост:", min(a))
