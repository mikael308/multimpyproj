

class DimenResource:
    """
    resource accessobject holding dimension attributes\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    top         = None
    right       = None
    bottom      = None
    left        = None
    linespacing = None
    dist        = None
    width       = None
    height      = None
    x           = None
    y           = None
    size        = None
    radius      = None
    border      = None

    def __init__(self):
        pass

    def pos(self):
        """
        get a coordinate position from this resource values\n
        :return:
        """
        return self.x, self.y

    def wh(self):
        """
        get tuple of width, height\n
        needs attributes
         * width
         * height
        :return:
        """
        return self.width, self.height

    def area(self):
        """
        calculates and get the area from this dimension\n
        needs attributes
         * width
         * height
        :return: dimensions area
        """
        return self.width * self.height

    def directions(self):
        """
        get tuple of this dimensions direction attributes\n
        needs attributes:
         * top
         * left
         * bottom
         * right
        :return: top, left, bottom, right
        """
        return self.top, self.right, self.bottom, self.left

    def diameter(self):
        """
        get the diameter of this dimension\n
        needs attributes:
         * radius
        :return:
        """
        return self.radius * 2

    def perimeter(self):
        """
        get the circumference of this dimension\n
        needs attributes:
         * radius
        :return:
        """
        from math import pi
        return self.diameter() * pi

