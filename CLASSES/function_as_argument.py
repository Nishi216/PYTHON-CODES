def function1(text):
    return text.upper()

def function2(text):
    return text.lower()

def greet(func):
    greeting = func('Function being passed as/'
                    'an argument')
    print(greeting)

greet(function1)
greet(function2)