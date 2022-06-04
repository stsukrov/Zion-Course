x = (int(input()))
y = 2

if x == 1:
    print('true')
while y < x:
    if x%y == 0:
        print('false')
        break
    else:
        y+=1
    if y == x:
        print('true')