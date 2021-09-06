def decorator(func):
    def inner(*args,**kwargs):
        print("Before Execution")
        result = func(*args,**kwargs)
        print("After Execution")
        return result
    return inner

@decorator
def sum_two_numbers(a,b):
    print("Inside the function")
    return a+b

a,b=1,2
print("Sum is:  ",sum_two_numbers(a,b))

