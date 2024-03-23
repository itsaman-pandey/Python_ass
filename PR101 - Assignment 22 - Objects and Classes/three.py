class Floor:
    def __init__(self, width: float, length: float):
        self.width = max(0.0, width)
        self.length = max(0.0, length)
    
    def get_area(self) -> float:
        return self.width * self.length

class Carpet:
    def __init__(self, cost_per_sq_meter: float):
        self.cost_per_sq_meter = max(0.0, cost_per_sq_meter)
    
    def get_cost(self) -> float:
        return self.cost_per_sq_meter

class Calculator:
    def __init__(self, floor: Floor, carpet: Carpet):
        self.floor = floor
        self.carpet = carpet
    
    def get_total_cost(self) -> float:
        return self.floor.get_area() * self.carpet.get_cost()