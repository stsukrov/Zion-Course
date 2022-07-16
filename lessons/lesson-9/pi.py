def PI(x):
   pi=0
   a=1
   for i in range(x):
       if i%2==0:
           pi+=4/a
           a+=2
       else:
           pi-=4/a
           a+=2
   return pi

print(PI(1000000))
