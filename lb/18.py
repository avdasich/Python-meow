j = input("Введите двоичное число: ")

a, b = 0, 0
for i in range(len(j) -1, -1, -1):
        if j[i] == '1':        a += 2**b
        b+=1
        print(a)
