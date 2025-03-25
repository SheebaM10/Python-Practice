book = {}

book['tom'] = {
    "name": "tom",
    "address": "1 red street"
}

book['bob'] = {
    "name": "bob",
    "address": "2 white street"
}

import json
s=json.dumps(book)
with open("c://data//book.txt", "w") as f:
    f.write(s)
    
    
f=open("c://data//book.txt", "r")
s=f.read()
print(s)

book=json.loads(s)
print(book)
print(type(book))
print(book['bob']['address'])

for person in book:
    print(book[person])
    