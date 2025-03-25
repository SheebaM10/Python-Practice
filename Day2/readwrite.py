# f=open("c:\\data\\funny.txt", "a")

# f.write("\nI Love Python")
# f.close()

f=open("c:\\data\\funny.txt", "r")
f_out =open("c:\\data\\fun.txt","w")
# print(f.read())
# f.close()

for line in f:
    tokens = line.split(' ')
    f_out.write("wordcount:"+ str(len(tokens))+line)
    # print(len(tokens))
    
f.close() 
f_out.close()
 