# __repr__ and __str__  for printing the objects

class test:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "test a:%s b:%s"%(self.a,self.b)

    def __str__(self):
        return "from str - test a:%s and b:%s"%(self.a,self.b)

object = test(50,80)
print([object])   #this calls __repr__
print(object)  #this calls __str__
