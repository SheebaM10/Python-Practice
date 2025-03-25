key_location ="chair"

location = ['living room', 'chair','kitchen', 'tv room', 'bed']

for i in location:
    if i==key_location:
        print("key is found in ", i)
        break
    else:
        print("key is not found in", i)