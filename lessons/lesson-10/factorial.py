def factorial(n):
  """Функция вычисляющая факториал по формуле:

  n! = (n-1)! * n

  Примеры:

    print(factorial(1)) -> 1
    print(factorial(3)) -> 6
    print(factorial(5)) -> 120
  """
  # Конечное условие, где 1! = 1.
  # Здесь рекурсия прерывается.
  if n == 1:
    return 1

  # Вычисляем факториал по формуле
  return n * factorial(n - 1)

print(factorial(1))
print(factorial(6))
print(factorial(5))
