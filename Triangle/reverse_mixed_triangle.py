rows = 5

for i in range(rows):
    for j in range(i, rows):
        print("*", end=" ")
    for j in range(i + 1):
        print(" ", end=" ")
    print()
print("---------------------------")
for i in range(rows,0,-1):
    for j in range(i):
      print("*",end=" ")
    print()    