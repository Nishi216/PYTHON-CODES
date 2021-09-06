#creating and calling class variables and object variables

class Dog:
    species = "mammal"
    def __init__(self,name):
        self.name = name

Coco = Dog("Coco")
Tom = Dog("Tom")

print('My name is {} and I am {}'.format(Coco.name,Coco.__class__.species))
print('My name is {} and I am {}'.format(Tom.name,Tom.species))