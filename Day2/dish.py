indian= ["samosa","daal", "naan"]
chinese=["egg role","pot sticker", "fried rice"]
italian=["pizza","pasta", "risotto"]

dish= input("Enter a dish name:")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("I dont know which cuisine is", dish)
    