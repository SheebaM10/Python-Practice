pal = input("Enter the string:")

def Palindrome(pal):
    if(pal==(pal[::-1])):
        print(pal, "Is Palindrome")
    else:
        print(pal, "Is not plaindrome")

Palindrome(pal)