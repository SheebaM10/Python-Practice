rows= 3
 
for i in range(rows):
    for j in range(rows- i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == i:
            print("1", end="")
        else:
            print("0", end="")
    print()