# class Father():
#     def gardening(self):
#         print("I enjoy gardening")
        
# class Mother():
#     def cooking(self):
#         print("I love cooking")
   
# class child(Father, Mother):
#     def sports(self):
#         print("I enjoy sports")
        
# c = child()
# c.gardening()
# c.cooking()
# c.sports()


class Father():
    def skills(self):
        print("gardening")
        
class Mother():
    def skills(self):
        print("cooking")
   
class child(Father, Mother):
    def skills (self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")
        
c = child()
c.skills()