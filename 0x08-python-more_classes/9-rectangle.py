#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Methods in class Rectangles"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self) -> str:
        """returns Reactangle"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            for j in range(self.width):
                string += str(self.print_symbol)
            if i != self.height - 1:
                string += "\n"
        return string

    def __repr__(self) -> str:
        """repr meothod"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """destructor"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """add static method to check biggest area of Rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle"""
        return cls(size, size)
