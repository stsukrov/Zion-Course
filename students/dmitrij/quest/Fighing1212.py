from secrets import choice
import random
mhp=0
mstreght=0
enemyhp=0
enemystreght=0
enemychar=random.randint(1,2)
if enemychar==1:
    enemyhp=180
    enemystreght=20
else:
    enemyhp=120
    enemystreght=30
print("Приветствую гладиатора!Скоро начнётся бой, скорее выберете вашего гладиатора:")
print("1.Живучий(20сила/180жизнь)") 
print("2.Сильный(30сила/120жизни)")
char = 0
while True:
    char=int(input())
    if char==1:
        mhp=180
        mstreght=20
    elif char==2:
        mhp=120
        mstreght=30
    else: 
        print("Введите число 1 или 2")
        char=int(input())
        continue
    break
while enemyhp>0 and mhp>0:
    print("Вот и начался бой гладиаторов")
    print("Вы можете атаковать(1) защищаться(2) уклониться(3)")
    print("Как только здоровье противника опуститься ниже 0 вы победите, в обратном случае проиграете")
    print(f"Здоровье противника:{enemyhp}")
    print(f"Ваше здоровье:{mhp}")
    mturn=int(input("Выберете ваше действие"))
    if mturn==1:
        break
    else:
        print("Вы воняете")