"Encapsulation"

class Point:
    "Point"

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self._z = z

    def set_coord(self, x, y, z):
        "set_coord"
        self.__x = x
        self.__y = y
        self._z = z

    def get_coord(self):
        "get_coord"
        return self.__x, self.__y, self._z


pt = Point(1,2,3)
print(pt.get_coord())
pt.set_coord(10,20,30)
print(pt.get_coord())
print(pt._z) #Можно вывести но не стоит, так как protected атрибуты служат для взаимодействия внутри дочерних и прородителя классов

#print(pt.__x, pt.__y) - нельзя вывести ошибка->(AttributeError: 'Point' object has no attribute '__x')