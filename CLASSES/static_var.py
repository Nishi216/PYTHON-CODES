# to demonstrate the use of class variable or static variable

class Student:
    stream = 'computer'
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

stud1 = Student('ABC',12)
stud2 = Student('DEF',22)

#accessing class variable via object name
print(stud1.stream, stud1.name, stud1.roll)
print(stud2.name, stud2.roll, stud2.stream)

#accessing class variable via class name
print(Student.stream)

#changing value of class variable for one object
stud1.stream = 'electrical'
print(stud1.stream, stud1.name)
print(stud2.stream, stud2.name)

#changing the class variable for all objects
stud3 = Student('HGI',32)
Student.stream = 'CSE'
print(stud1.stream,stud1.name)
print(stud2.stream, stud2.name)
print(stud3.stream, stud3.name)