# Class README

## Wall Class
The `Wall` class represents a wall with a given width and height. It provides methods to set and get the width and height, as well as to calculate the area of the wall.

### Constructors:
- `Wall()`: Initializes a wall with a width and height of 0.0.
- `Wall(width: float, height: float)`: Initializes a wall with the given width and height. If either the width or height is less than 0, it is set to 0.0 instead.

### Methods:
- `get_width() -> float`: Returns the width of the wall.
- `get_height() -> float`: Returns the height of the wall.
- `set_width(width: float)`: Sets the width of the wall. If the parameter is less than 0, the width is set to 0.0.
- `set_height(height: float)`: Sets the height of the wall. If the parameter is less than 0, the height is set to 0.0.
- `get_area() -> float`: Calculates and returns the area of the wall (width * height).

## Point Class
The `Point` class represents a point in a 2D space with x and y coordinates. It provides methods to set and get the coordinates, as well as to calculate distances between points.

### Constructors:
- `Point()`: Initializes a point at (0, 0).
- `Point(x: int, y: int)`: Initializes a point with the given x and y coordinates.

### Methods:
- `get_x() -> int`: Returns the x-coordinate of the point.
- `get_y() -> int`: Returns the y-coordinate of the point.
- `set_x(x: int)`: Sets the x-coordinate of the point.
- `set_y(y: int)`: Sets the y-coordinate of the point.
- `distance() -> float`: Calculates and returns the distance between this point and the origin (0, 0).
- `distance(x: int, y: int) -> float`: Calculates and returns the distance between this point and the point with the given coordinates.
- `distance(other_point: Point) -> float`: Calculates and returns the distance between this point and the given point.

## Carpet Company Classes
These classes represent a carpet company's system for calculating the cost of carpeting for rectangular rooms.

### Floor Class
The `Floor` class represents a rectangular floor with given width and length. It provides a method to calculate the area of the floor.

### Constructors:
- `Floor(width: float, length: float)`: Initializes a floor with the given width and length. If either the width or length is less than 0, it is set to 0.0 instead.

### Methods:
- `get_area() -> float`: Returns the area of the floor (width * length).

### Carpet Class
The `Carpet` class represents a carpet with a given cost per square meter.

### Constructors:
- `Carpet(cost_per_sq_meter: float)`: Initializes a carpet with the given cost per square meter. If the cost is less than 0, it is set to 0.0 instead.

### Methods:
- `get_cost() -> float`: Returns the cost per square meter of the carpet.

### Calculator Class
The `Calculator` class represents a calculator for determining the total cost of carpeting a floor with a given carpet.

### Constructors:
- `Calculator(floor: Floor, carpet: Carpet)`: Initializes a calculator with the given floor and carpet.

### Methods:
- `get_total_cost() -> float`: Calculates and returns the total cost to cover the floor with the carpet.

