n = int(input("enter a no:"))

for i in range(3,n):
    if (i%3):
        print(n, "divisible by 3")
        break
else:
        print(n, "not divisble by 3")