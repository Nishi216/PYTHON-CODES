def decor1(func):
    def inner():
        x = func()
        print("This decorator is applied first")
        return x*x
    return inner

def decor2(func):
    def inner():
        x=func()
        print("Then this decorator is applied")
        return 2*x
    return inner

@decor2
@decor1
def num():
    return 10

print(num())