

class Buffer:
    """
    buffer containing elements of specific capacity\n
    the index uses linear hashprobing\n

    :author: Mikael Holmbom
    :ver: 1.0
    """

    __elements      = None
    __capacity      = 0

    __idx           = 0
    __idx_hashkey   = 3

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("buffer capacity must be a positive number")

        # set hashkey
		primes = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67}
		if capacity < 3:
			self.__idx_hashkey = 1
		else:
			for p in primes:
				if not capacity % p == 0:
					self.__idx_hashkey = p
					break
			else:
				self.__idx = 1

        self.__capacity = capacity
        self.__elements = {}

    def __getitem__(self, item):
        if item >= self.__capacity:
            raise IndexError("index [" + str(item) + "] out bounds, buffer capacity: " + str(self.__capacity))

        return self.__elements.get(item, None)

    def __len__(self):
        return len(self.__elements)

    def __iter__(self):
    	"""
    	iterate over buffers values
    	"""
        return self.__elements.itervalues()

    def __contains__(self, item):
    	"""
    	determine if buffer contains item
    	"""
        return item in self.__elements.values()

    def __delitem__(self, key):
        del self.__elements[key]

    def __str__(self):
        l = self.__elements.items()
        l.sort()

        s = "[ "

        for i, e in enumerate(l):
            s += "[" + str(e[0]) + "]" + ":" + str(e[1])
            if i < len(self.__elements):
                s += ", "
        s += " ]"
        s += "{" + str(self.get_size()) + "/" + str(self.__capacity) + "}"

        return s

    def get_capacity(self):
        """
        get the capacity of this Buffer
        :return:
        """
        return self.__capacity

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

    def __next_hash(self):
        """
        get the next hash index\n
        :return:
        """
        self.__idx += self.__idx_hashkey
        self.__idx %= self.__capacity
        return self.__idx

    def clear(self):
    	"""
    	clear the elements in this buffer
    	"""
    	self.__elements.clear()
    	return self.is_empty() == True
    	
    def add(self, item):
        """
        add item to this Buffer
        :param item: item to add
        :return: True if item was added
        """
        if not self.is_full():
            for i in range(0, self.__capacity):
                idx = self.__next_hash()

                if not self.__elements.has_key(idx):
                    self.__elements[idx] = item
                    return True

        return False

    def deleteAt(self, idx):
    	"""
    	delete element at requested index
    	:param idx: index to delete
    	:return: True if element was not empty and is now deleted
    	"""
    	if self.__elements.has_key(idx):
    		del self.__elements[idx]
    		if not self.__elements.has_key(idx):
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
        :return: True if there is no elements in this buffer
        """
        return self.get_size() == self.__capacity
