# Введите число и вычислите сколько раз его можно удвоить пока оно не привысит 100

x = int(input("Введите число: "))

cnt = 0

while 2*x <= 100:
    x = x * 2
    cnt = cnt + 1

print(cnt)