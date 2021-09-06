"""
def outer_func(*args,**kwargs):
    def inner(func)
        '''Operation on the function'''
        return func
    return inner ''' This will return the object for outer_func'''

@outer_func(parameters)
def func():
    ''' function implementation '''
"""

def decorator(x,y):
    def inner(func):
        def wrapper(*args,**kwargs):
            print("I like python")
            print("Sum of numbers :  ",x+y)
            func(*args,**kwargs)
        return wrapper
    return inner

@decorator(12,20)
def my_func(*args):
    for ele in args:
        print(ele)

#decorator(12,20)(my_func)('python','is','amazing')
my_func('python','learning')