def addition(x):
    def sub_add(y):
        return x+y
    return sub_add

add_value = addition(10)
print(add_value(20))