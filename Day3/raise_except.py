class Accident (Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_expection (self):
        print("User defined expception:", self.msg)

try:
    raise Accident('Car crash')
except Accident as e:
    e.print_expection()
    