

class FontResource:
    """
    resource access object holding data about font\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    name        = ""
    size        = 0

    def __init__(self, name, size):
        """
        initiate this attributes name, size
        :param name:
        :type name: str
        :param size:
        :type size: int
        """
        self.name = name
        self.size = size
