#CREATING CLASSES AND OBJECTS IN PYTHON

class Android:
    def define_self(self):
        print("hello my name is " + self.name + " I am " + self.color + " and I weigh " + self.weight + "kg") #self is the same as this in javascript



A1 = Android() ## A1 is now an object
A1.name = "Android Jimmy"
A1.color = "orange"
A1.weight = str(30)
A1.define_self()