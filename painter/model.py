# TODO: Add code here
import math
import matplotlib.pyplot as plt
import pickle

class Point:
    def __init__(self, x:float, y:float) -> None:
        self.x=x
        self.y=y

class Circle:
    def __init__(self, center:Point, radius:float) -> None:
        self.center=center
        self.radius=radius
    def area(self) -> float:
        area= math.pi * (self.radius**2)
        return area
    def draw(self) -> None:
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()
    def __str__(self) -> str:
        return f"Circle with center at ({self.center.x},{self.center.y}) and radius {self.r}"

class Triangle:
    def __init__(self, point_1:Point, point_2:Point, point_3:Point) -> None:
        self.point_1=point_1
        self.point_2=point_2
        self.point_3=point_3
    
    def area(self) -> float:
        area = abs(self.point_1.x*(self.point_2.y - self.point_3.y) + self.point_2.x*(self.point_3.y - self.point_1.y) + self.point_3.x*(self.point_1.y - self.point_2.y)) / 2
        return area
    
    def draw(self) -> None:
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()
    
    def __str__(self) -> str:
        return f"Triangle with vertices at ({self.point_1.x},{self.point_1.y}),({self.point_2.x},{self.point_2.y}) and ({self.point_3.x},{self.point_3.y})"

class Rectangle:
    def __init__(self, point_1:Point, point_2:Point) -> None:
        self.point_1=point_1
        self.point_2=point_2
    
    def area(self) -> float:
        x_side = abs(self.point_2.x - self.point_1.x)
        y_side = abs(self.point_2.y - self.point_1.y)
        area = x_side * y_side
        return area
    
    def draw(self) -> None:
        x = [self.point_1.x, self.point_2.x, self.point_2.x, self.point_1.x, self.point_1.x]
        y = [self.point_1.y, self.point_1.y, self.point_2.y, self.point_2.y, self.point_1.y]
        plt.fill(x, y, color='g')
        plt.axis("scaled")
        plt.show()
    
    def __str__(self) -> str:
        return f"Rectangle with vertices at ({self.point_1.x},{self.point_1.y}) and ({self.point_2.x},{self.point_2.y})"
    
class Painter:
    
    FILE = ".painter"
    
    def __init__(self) -> None:
        self.shapes: list = []
        self._load()

    def _load(self) -> None:
        try:
            with open(Painter.FILE, "rb") as f:
                self.shapes = pickle.load(f)
        except (EOFError, FileNotFoundError):
            self.shapes = []
    
    def _save(self) -> None:
        with open(Painter.FILE, "wb") as f:
            pickle.dump(self.shapes, f)
    
    def add_shape(self, shape) -> None:
        self.shapes.append(shape)
        self._save()

    def total_area(self) -> float:
        return sum(shape.area() for shape in self.shapes)
    
    def clear(self) -> None:
        self.shapes = []
        self._save()