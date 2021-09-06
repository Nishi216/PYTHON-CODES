#Data hiding and data accessing

class myclass:
    __hidden = 1
    def add(self,value):
        self.__hidden += value
        print(self.__hidden)

object = myclass()
object.add(2)
object.add(5)
print('To access from outside:    ',object._myclass__hidden)