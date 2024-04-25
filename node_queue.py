import node

class Queue:
    slots = ["__front", "__back", "__size"]

    def __init__(self):
        self.__front = None
        self.__back = None
        self.__size = 0

    def size(self):
        return self.__size

    def peek(self):
        if self.__front is None:
            raise IndexError("peek on empty queue")
        else:
            return self.__front.get_value()

    
    def dequeue(self):
        if self.__front is None:
            raise IndexError("peek on empty queue")
        front = self.__front
        value = front.get_value()
        self.__size -= 1
        self.__front = front.get_next()

        if self.__front is None:
            self.__back = None

        return value
    
    def enqueue(self, value):
        new_back = node.Node(value)
        if self.__front is None:
            self.__front = new_back
        else:
            self.__back.set_next(new_back)
        self.__back = new_back
        self.__size += 1

    def is_empty(self):
        return self.__front is None

    def __str__(self):
        string = "["
        node = self.__front
        if node is not None:
            string += str(node.get_value())
            node = node.get_next()
            while node is not None:
                string += ", " + str(node.get_value())
                node = node.get_next()
        string += "]"
        return string