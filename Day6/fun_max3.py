n1= int(input("enter the no1: "))
n2= int(input("enter the no2: "))
n3= int(input("enter the no3: "))

def Max(n1,n2,n3):
    if(n1>=n2 and n1>=n3):
        print(n1, "is greater")
    elif(n2>=n3 and n2>=n1):
        print(n2, "is greater")
    else:
        print(n3, "is greater")
        
Max(n1,n2,n3)