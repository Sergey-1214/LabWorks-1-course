class Circle:
    def __init__(self,radius:int):
        self.radius = radius
    def get_radius(self)->int:
        return self.radius
    def set_radius(self,new_radius:int):
        self.radius = new_radius

my_circle = Circle(5)
my_circle.set_radius(7)
print(my_circle.get_radius())
