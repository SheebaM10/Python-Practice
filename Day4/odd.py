# rows=4
# k=0
# for i in range(0,rows+1):
#     for j in range(1+i):
#         k=k+2
#         print(k, end=" ")
        
#     print('')


# rows=10
# k=1
# for i in range(0,rows+1):
#     for j in range(1+i):
      
#         print(k, end=" ")
#         k=k+2
#     print('')

# rows=6

# for i in range(0,rows+1):
#     for j in range(rows,i+1,-1):

#         print(j, end=" ")
#     print('')
    
# for i in range (10,0,-1):

#     a=" "
#     for j in range(0,i+1):
#         a= a+" "+str(j)
#     print(a)
    
# for i in range (10,0,-1):

#     a=" "
#     for j in range(i-1):
#         a = " "+a+str(j)
#     print(a)
# print(' ')

n=6
for i in range(1,n+1):
   num=1
   for j in range(n,0,-1):
      if j>i :
         print(" ", end=" ")
      else:
         print(num, end=" ")
         num+=1
   print()
 

 