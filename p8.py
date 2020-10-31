rows = 5
k = 2 * rows - 2
for i in range(0,rows):
    for j in range(0,k):
        print(end=' ')
    k -=1
    for j in range(0,i+1):
        print('* ',end='')
    print()
k = rows - 2
for i in range(rows,1,-1):
    for j in range(k,-2,-1):
        print(end=' ')
    k +=1
    for j in range(1, i):
        print('* ',end='')
    print()
