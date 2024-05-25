#!/usr/bin/python3

class Node:
    """Defines a single node
    """
    def __init__(self, data, next_node):
        """Initialise Node

        Args:
            data (_int_)        : Given node data
            next_node (_Node_)  : Next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Get `data`

        Returns:
            _int_: `data` property
        """
        return self.__data

    @property
    def next_node(self):
        """Get `next_node`

        Returns:
            _Node_:  `next_node` property
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """ Set data w a given value

        Args:
            value (_int_): Integer

        Raises:
            TypeError: If value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """ Set next_node w given value

        Args:
            value (_Node_): Node object. Error handling

        Raises:
            TypeError: _description_
        """
        if not isinstance(value, Node):
            raise TypeError("next_node must be a valid Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Defines a singlylinked list

    Attributes:
        __head  : List head. Defaults to `None`

    Methods:
        `sorted_insert(self, value)`    : Sort nodes
        `__str__(self)`                 : Return printable data
    """
    def __init__(self):
        """Initialise list. `head` defaults to `None`
        """
        self.__head = None

    def sorted_insert(self, value):
        """ Sorts nodes upon insertion

        Args:
            value (_Node_): New node
        """
        new_node = Node(self, value)
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            temp2 = temp.next_node

            while temp and temp2 and (temp2.data < value):
                temp = temp.next_node
                temp2 = temp.next_node

            new_node.next_node = temp2
            temp.next_node = new_node

    def __str__(self):
        """ Prints node in ascending order

        Returns:
            _str_: Node data as string
        """
        temp = self.__head
        output = ""
        while (temp):
            output += str(temp.data)
            temp = temp.next_node
            if (temp):
                output += "\n"
        return output
