
#using pop(parameter is optional) - to pop out the element
fruits = ['apple','banana','citrus','egg','guava','pomegranate','kiwi']
x=fruits.pop()       #last element will be popped out
print(x)
x=fruits.pop(3)      #element at index 3 will be popped out
print(x)
print()


#using remove(element) - name of the element to remove is given
print(fruits)
fruits.remove('apple')
print(fruits)