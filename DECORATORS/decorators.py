#Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.
"""
def modification(func):
    def inner_func():
        print("This line will be added first")
        func()
        print("This line will be added at last")
    return inner_func

def function_to_modify():
    print("This is an existing function which we will modify")

function_to_modify = modification(function_to_modify)
function_to_modify()
"""

import time
import math
def time_taken(func):
    def inner(*args,**kwargs):
        begin = time.time()
        func(*args,**kwargs)
        end= time.time()
        print("Time taken is : ",func.__name__,end-begin)
    return inner
@time_taken
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(10)
