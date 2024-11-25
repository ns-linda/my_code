class Node:
    def __init__(self, value):
        self.value=value
        self.right=None
        self.left = None

class Tree:
    def __init__(self):
        self.root=None

    def pprint(self):
        if self.root is not None:
            self.__pprint(self.root)

    def __pprint(self, Node):
        if Node !=None:
            self.__pprint(Node.left)
            print(Node.value)
            self.__pprint(Node.right)

    def add(self, value):
        if self.root is None:
            self.root= Node(value)
        else:
            self.__add(value,self.root)

    def __add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self.__add(value, node.left)
            else:
                node.left=Node(value)
        else:
            if node.right is not  None:
                self.__add(value, node.right)
            else:
                node.right = Node(value)

bt= Tree()
bt.add(10)
bt.add(30)
bt.add(20)
bt.pprint()


