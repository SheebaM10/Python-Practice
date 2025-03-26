rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if j == 2 or i == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
