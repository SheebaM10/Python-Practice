num = int(input("Enter the number: "))

s ={0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

def NumberWord(n):
    words = []
    for i in str(n):
        words.append(s[int(i)])
    print(" ".join(words))
        
NumberWord(num)