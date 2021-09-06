#In Python, we can define a function inside another function.
#In Python, a function can be passed as parameter to another function

def python(text):
    def welcome():
        return "Hello World! "
    return welcome()+"You are learning "+text

print(python("python"))

#A decorator is a function that takes a function as its only parameter and returns a function.
