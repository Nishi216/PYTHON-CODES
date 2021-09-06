#defining the concept of inheritance

class person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print('My name is  {}'.format(self.name))
        print('Id number:  {}'.format(self.idnumber))


class employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post = post
        person.__init__(self,name,idnumber)

    def details(self):
        print('My name is  {}'.format(self.name))
        print('Id number:  {}'.format(self.idnumber))
        print('I get a salary of:   ',self.salary)
        print('I am in post:   ',self.post)

tom = employee('Tom',1234,30000,"analyst")
tom.display()
tom.details()