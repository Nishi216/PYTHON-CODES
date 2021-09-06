def decorator(func):
    func.data = "python"
    return func

@decorator
def function(x,y):
    return x+y

print(function(10,20))
print(function.data)
