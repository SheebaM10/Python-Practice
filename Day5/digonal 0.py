rows = 5

for i in range( 0,rows):
    for j in range (0, rows):
        if ((i==j)):
            print("0", end= " ")
        elif(i+j==rows-1):
            print("0", end= " ")
        else:
            print("1", end= " ")
    print('')
    
    
    # 0,4
    # 1,3
    # 2,2
    # 3,1
    # 4,0