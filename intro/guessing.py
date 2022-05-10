import random

num = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Угадай число "))

    if guess == num:
        print("Правильно!")
        break
    elif guess > num:
        print("Мое меньше!")
    else:
        print("Мое больше!")

    attempts = attempts + 1

print(f"Ты угадал число с {attempts} попытки")

