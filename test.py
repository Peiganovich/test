"classmethod_and_staticmethod"

class Vector:
    "Coords"
    MAX_COORDS = 100
    MIN_COORDS = 0

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    @classmethod
    def validate(cls, arg):
        "Validate"
        return cls.MIN_COORDS <= arg <= cls.MAX_COORDS

    @staticmethod
    def norm2(x, y):
        "Norm2"
        return x*x + y*y



vector = Vector(1,2)
print(Vector.norm2(5,6))
print(Vector.validate(vector.x))
