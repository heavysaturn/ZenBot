from .vectors import Vector3

class GameObject:
    def __init__(self):
        self.location = Vector3([0, 0, 0])
        self.velocity = Vector3([0, 0, 0])
        self.rotation = Vector3([0, 0, 0])
        self.rvelocity = Vector3([0, 0, 0])
        self.local_location = Vector3([0, 0, 0])