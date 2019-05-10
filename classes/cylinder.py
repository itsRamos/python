# Cylinder class with methods to calculate volume and surface area
class Cylinder:

    # pi = 3.1416
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return (Cylinder.pi * (self.radius**2) * self.height)
    
    def surface_area(self):
        return ((2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * (self.radius**2)))


if __name__ == '__main__':
    c = Cylinder(2,3)
    
    print(c.volume())
    print(c.surface_area())
