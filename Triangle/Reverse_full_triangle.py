rows = 5
for i in range(rows):
    for j in range(rows, rows - i, -1):
        print("", end=" ")
    for j in range(rows,i,-1):
        print("*",end=" ")
    print()  