def decorator(func):
    def welcome(text):
        return "Welcome to "+func(text)
    return welcome

@decorator
def python(text):
    return text

print(python("python"))