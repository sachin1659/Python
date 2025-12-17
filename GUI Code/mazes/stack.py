class Stack:
    """  pass keyword   you have to add pass in an empty class otherwise you get the error"""

    def __init__(self):
        """init is constructor used for creating object of class Stack"""
        self.items = []
        """the items properties of the object that we are creating, self refers to specific instance of the class"""

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        """this method returns the string representation of the object"""
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(1)
    print(s)
    s.push(5)
    s.push(4)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    """returns the last item in the stack"""
    print(s.size())
    """returns the size of the stack"""
