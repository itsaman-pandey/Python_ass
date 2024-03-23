# Point Class
# The Point class represents a point in a 2D space with x and y coordinates. It provides methods to set and get the coordinates, as well as to calculate distances between points.

# Constructors:
# Point(): Initializes a point at (0, 0).
# Point(x: int, y: int): Initializes a point with the given x and y coordinates.
# Methods:
# get_x() -> int: Returns the x-coordinate of the point.
# get_y() -> int: Returns the y-coordinate of the point.
# set_x(x: int): Sets the x-coordinate of the point.
# set_y(y: int): Sets the y-coordinate of the point.
# distance() -> float: Calculates and returns the distance between this point and the origin (0, 0).
# distance(x: int, y: int) -> float: Calculates and returns the distance between this point and the point with the given coordinates.
# distance(other_point: Point) -> float: Calculates and returns the distance between this point and the given point.

class Point:
    def __init__(self,a=0.0,b=0.0):
        self.x = a
        self.y = b
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_x(self,a):
        self.x = a
    def set_y(self,a):
        self.y = a
    def distance(self,a = 0.0, b = 0.0):
        d = (self.x-a)**2 + (self.y-b)**2
        d = d**0.5
        return d
    def distance(self,other):
        d = (self.x-other.x)**2 + (self.y-other.y)**2
        d = d**0.5
        return d

point1 = Point(3, 4)

x_coordinate = point1.get_x()
y_coordinate = point1.get_y()

point1.set_x(5)
point1.set_y(6)

origin = Point()

distance_from_origin = point1.distance(origin)
dis = point1.distance(0,0)


