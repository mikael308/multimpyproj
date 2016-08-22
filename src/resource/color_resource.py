

class ColorResource:
    """
    resource access object holding data describing a color as of RGB values\n

    :author: Mikael Holmbom
    :version: 1.0
    """
    # RED value
    r = 0
    # GREEN value
    g = 0
    # BLUE value
    b = 0

    def __init__(self, r, g, b):
        """

        :param r: red
        :type r: int
        :param g: green
        :type g: int
        :param b: blue
        :type b: int
        """
        self.r = r
        self.g = g
        self.b = b

    def rgb(self):
        """
        get the red, green, blue value as a tuple\n
        :return:
        """
        return (self.r, self.g, self.b)

    def __str__(self):
        return "(r"+str(self.r) +", g" + str(self.g) + ", b" + str(self.b) + ")"

