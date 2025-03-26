num = int(input("Enter the number: "))

def Sum(num):
    s=0
    while(num>0):
        rem=num%10
        s=s+rem
        num= num//10
    print(s)

Sum(num)

    
    