import time

def calc_square(numbers):
    print("calculate square nos")
    for n in numbers:
        time.sleep(0.2)
        print( "square", n*n)
        
def calc_cube(numbers):
    print("calculate cube nos")
    for n in numbers:
        time.sleep(0.2)
        print( "cube", n*n*n)
        
arr = [2,3.8,9]

t= time.time()
calc_square(arr)

print ("done in:", time.time() -t)
print ("haha...")