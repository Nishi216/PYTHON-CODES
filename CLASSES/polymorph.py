
class India():
    def capital(self):
        print('Delhi is the capital')
    def language(self):
        print('People normally speaks in Hindi')

class USA():
    def capital(self):
        print('Washington is the capital')
    def language(self):
        print('People normally speaks in English')

def func(obj):
    obj.capital()
    obj.language()

objind = India()
objusa = USA()

func(objind)
func(objusa)