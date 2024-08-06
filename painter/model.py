# TODO: Add code here
import math

class Point:
    def __init__(self, x:float, y:float):
        self.x=x
        self.y=y

class Circle:
    def __init__(self, center:Point, radius:float):
        self.center=center
        self.radius=radius
    def area(self) -> float:
        area= math.pi * (self.radius**2)
    