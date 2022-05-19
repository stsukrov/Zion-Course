# Вычислить факториал целого числа

n = int(input("Введите число: "))

result = 1
while n > 1:
    result = result * n
    n = n - 1

print(result)