def name(text):
    return text.upper()

print(name('Nishi Paul'))

another_function = name

print(another_function('Nishi Paul'))

#Here another_function is pointing to the same function object
# as pointed by the name function.