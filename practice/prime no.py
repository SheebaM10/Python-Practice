# n = int(input("enter the no:"))
# n1=0
# for i in range(2,(n//2)+1):
#     if n%i==0:
#         n1=1
#         break
# if n1==0:
#     print ("prime")   
# else:
#     print("not prime")



n = int(input("enter the no:"))

for i in range(2,n):
    if ((n%i)==0):
        print(n, "is not prime")
        break
else:
        print(n,"is prime")
        