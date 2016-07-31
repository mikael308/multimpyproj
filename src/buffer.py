

class Buffer:
    """
    :author: Mikael Holmbom
    :ver: 1.0
    """

    __elements      = {}
    __capacity      = 0

    __idx           = 0

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("buffer capacity must be a positive number")

        self.__capacity = capacity

    def get_capacity(self):
        """
        get the capacity of this Buffer
        :return:
        """
        return self.__capacity

    def __len__(self):
        return len(self.__elements)

    def __contains__(self, item):
        return self.__elements.__contains__(item)
    def __str__(self):
        l = self.__elements.items()
        l.sort()

        s = "[ "
        i = 0
        for e in l:
            i += 1
            s += str(e[0]) + ":" + str(e[1])
            if i < len(self.__elements):
                s += ", "
        s += " ]"
        s += "{" + str(self.__capacity) + "}"

        return s

    def get_size(self):
        """
        get size of this Buffer, that is current amount of elements
        :return:
        """
        return len(self.__elements)

    def index(self, item):
        """
        get the item element index from this Buffer
        :param item: item to determine index
        :return: the index of item, if item is not found None is returned
        """
        for key, value in self.__elements.items():
            if value == item:
                return key

    def add(self, item):
        """
        add item to this Buffer
        :param item: item to add
        :return: True if item was added
        """
        for i in range(0, self.__capacity):
            idx = self.__idx % self.__capacity
            self.__idx += 1

            if not self.__elements.has_key(idx):
                self.__elements[idx] = item
                return True

        return False

    def delete(self, elem):
        """
        delete element from this Buffer
        :param elem: element to delete
        :return: True if element was deleted
        """
        for key, value in self.__elements.items():

            if value == elem:
                del self.__elements[key]

                return True

        return False

    def is_empty(self):
        """
        determine if this Buffer is empty, that is has 0 elements
        :return: True if empty
        """
        return self.get_size() == 0

    def is_full(self):
        """
        determine if this Buffer is full, that is reached its max capacity
        :return:
        """
        return self.get_size() == self.__capacity


