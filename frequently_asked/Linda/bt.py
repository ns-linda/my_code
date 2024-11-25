class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class bt:
    def __init__(self):
        self.root = None

    def pprint(self):
        if self.root is not None:
            self.__print(self.root)

    def __print(self, Node):
        if Node is not None:
            self.__print(Node.left)
            print(Node.value)
            self.__print(Node.right)

    def add(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self.__add(value, self.root)

    def __add(self, value, node):
        if value < node.value:
            if node.left !=None:
                self.__add(value, node.left)
            else:
                node.left=Node(value)
        else:
            if node.right !=None:
                self.__add(value, node.right)
            else:
                node.right= Node(value)

b=bt()
b.add(10)
b.add(20)
b.add(40)
b.pprint()