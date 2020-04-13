

row=int(input("Enter the rows: "))
col=int(input("Enter the Cols: "))

for i in range(row):
    for j in range(col):
        print('*',end=' ')
    print()

row=int(input("Enter the rows: "))

for i in range(row+1):
    for j in range(i):
        print('*',end=' ')
    print()


