import math


def set_unit(unit):
    """Register a unit on a function"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit


@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius**2 * height


def main():
    print(volume(3, 5))

    print(volume.unit)


if __name__ == '__main__':
    main()


# The same result could be achieved with function annotations

# import math
#
# def volume(radius, height) -> "cm^3":
#     return math.pi * radius**2 * height