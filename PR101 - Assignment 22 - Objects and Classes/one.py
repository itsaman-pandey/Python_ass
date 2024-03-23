# Wall Class
# The Wall class represents a wall with a given width and height. It provides methods to set and get the width and height, as well as to calculate the area of the wall.

# Constructors:
# Wall(): Initializes a wall with a width and height of 0.0.
# Wall(width: float, height: float): Initializes a wall with the given width and height. If either the width or height is less than 0, it is set to 0.0 instead.
# Methods:
# get_width() -> float: Returns the width of the wall.
# get_height() -> float: Returns the height of the wall.
# set_width(width: float): Sets the width of the wall. If the parameter is less than 0, the width is set to 0.0.
# set_height(height: float): Sets the height of the wall. If the parameter is less than 0, the height is set to 0.0.
# get_area() -> float: Calculates and returns the area of the wall (width * height).

class Wall:

    def __init__(self):
        self.width = 0.0
        self.height = 0.0
    def __init__(self,x,y):
        self.width = x
        self.height = y
    def get_width(self):
        return self.width
    def get_width(self):
        return self.height
    def set_width(self,x):
        if x > 0:
            self.width = x
        else:
            self.width = 0.0    
    
    def set_height(self,y):
        if y>0:
            self.height = y
        else:
            self.height = 0.0
    def get_area (self):
        return self.height*self.width

a = Wall(2,3)
a.set_height(7)
a.set_width(8)
print(a.get_area())