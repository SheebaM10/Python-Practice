rows = 9

for i in range( 0,rows):
    for j in range (0, rows):
        if( (i==0)or(j==0)or(i==rows-1)or(j==rows-1)):
            print("1", end=" ")
        elif(i == rows // 2 and j == rows // 2): 
            print("1", end=" ")
        else:
            print("0", end=" ")
        
    print('')



    
    