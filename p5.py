rows = 5
for i in range(0, rows+1):
    print('*'*i,end=' ')
    print()
for i in range(rows,1,-1):
    for j in range(0,i-1):
        print('*',end='')
    print()
