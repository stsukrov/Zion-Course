# У героя 50 единиц здоровья из 100
max_health = 100
health = 50

# Каждый волшебный напиток дает 30 единиц здоровья.
drinks = 3

while True:
 cmd = input("Что будем делать? ")
 if cmd == "Выпить":
     if drinks > 0:
         drinks = drinks - 1
         health = health + 30
         if health > max_health:
             health = max_health

         print(f"В сумке {drinks} бутылок. Здоровье {health}/{max_health}")
     else:
         print("А нечего!")
 else:
     break

print("Пока!")

