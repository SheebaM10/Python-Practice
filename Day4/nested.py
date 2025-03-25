# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print('')

# rows = 4  # Number of rows in the pattern

# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1,i+1):  # Inner loop for columns
#         print(j, end=" ")  # Print '1' with a space
#     print('')  # Move to the next line


# rows = 5  

# for i in range(rows,0,-1):  
#     for j in range(rows,i-1,-1):  
#         print(i, end=" ")  
#     print('')  

rows = 5  

for i in range(rows,0,-1):  
    for j in range(rows,rows-i,-1):  
        print(j, end=" ")  
    print('')  