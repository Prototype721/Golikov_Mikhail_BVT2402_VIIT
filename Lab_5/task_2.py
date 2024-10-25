class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius



My_circle = Circle(5)

My_circle.set_radius(9)

print(My_circle.get_radius())
