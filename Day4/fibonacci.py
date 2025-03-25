n = int(input("Enter the number of terms: "))  
a, b = 0, 1  

for i in range(n):  
    print(a, end=" ")  # Print the current term  
    a, b = b, a + b  # Update a and b  
