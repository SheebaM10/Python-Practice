x=input("enter no1:")
y=input("enter no2:")
try: 
    z=x/int(y)
except ZeroDivisionError as e:
    print('Division by zero exception')
    z= None
except TypeError as e:
    print('type error')
    z= None
print("division is:", z)
 