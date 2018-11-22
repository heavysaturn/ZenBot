import math


class Vector3:
    def __init__(self, data):
        self.data = data

    def __sub__(self,value):
        return Vector3([
            self.x - value.x,
            self.y - value.y,
            self.z - value.z
        ])

    def __mul__(self, value):
        return (
            self.x * value.x
            + self.y * value.y
            + self.z * value.z
        )

    @property
    def x(self):
        return self.data[0]

    @property
    def y(self):
        return self.data[1]

    @property
    def z(self):
        return self.data[2]

    @property
    def pitch(self):
        return self.x

    @property
    def yaw(self):
        return self.y

    @property
    def roll(self):
        return self.z


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, val):
        return Vector2(self.x + val.x, self.y + val.y)

    def __sub__(self, val):
        return Vector2(self.x - val.x, self.y - val.y)