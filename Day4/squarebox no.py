rows = 3

for i in range (0, rows):
    for j in range (0, rows):
        if (i==1 and j==1):
            print("0", end = " ")
        else:
            print("1", end = " ")
    print(' ')