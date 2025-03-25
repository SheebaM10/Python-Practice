class Vehicle:
    def general_usage(self):
        print("general use: transporation")
        
class car(Vehicle):
    def __init__(self):
        print("Im car")
        self.wheels=4
        self.has_roof=True
        
    def specific_usage(self):
        print("specific use: commute to work, vacation with family")
        
        
class MotorCycle(Vehicle):
    def __init__(self):
        print("Im MotorCycle")
        self.wheels=2
        self.has_roof=True
        
    def specific_usage(self):
        print("specific use: road tip,racing")
        
c=car()
c.general_usage()
c.specific_usage()


m = MotorCycle()
m.general_usage()
m.specific_usage()

        
        