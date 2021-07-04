class Circle:
    def __init__(self, radius):
        self._radius = radius    # mutable property. can be set to a different value.

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    # by defining a setter method, we can do some error testing
    # Properties are accessed as attributes without parentheses
    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    # immutable property
    # properties without .setter() methods can’t be changed.
    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    # regular method
    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    #   Class method
    #   It’s not bound to one particular instance of Circle
    #  Class methods are often used as factory methods that can create specific instances of the class.
    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    #   static method
    #  It’s not really dependent on the Circle class, except that it is part of its namespace.
    #  Static methods can be called on either an instance or the class.
    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535


def main():
    c = Circle(5)
    print(c.radius)

    print(c.area)

    c.radius = 2
    print(c.area)

    try:
        c.area = 100
    except AttributeError as e:
        print(e)

    print(c.cylinder_volume(height=4))

    try:
        c.radius = -1
    except ValueError as e:
        print(e)

    c = Circle.unit_circle()
    print(c.radius)

    print(c.pi())

    print(Circle.pi())


if __name__ == '__main__':
    main()
