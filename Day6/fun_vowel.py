def Vowel(s):
    count=0
    for i in s:
        if i in "aeiuoAEIUO":
            count+=1
    print(count)
    
s= input("Enter the string: ")      
Vowel(s)
            
            