class Node:
    def __init__(self, data):
        self.data=data
        self.ref =None

class Linked:
    def __init__(self):
        self.head = None

    def print(self):
        n=self.head
        if n is  None:
            print("empty list")
        else:
            while n is not None:
                print(n.data)
                n=n.ref

    def addbegin(self, data):
        if self.head is None:
            self.head= Node(data)
        else:
            new_node=Node(data)
            new_node.ref=self.head.ref
            self.head=new_node

    def addend(self, data):
        n=self.head
        while n.ref is not None:
            n=n.ref
            break
        if n is not None:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def addmiddle(self, data, x):
        n=self.head
        while n.ref is not None:
            if x==n.data:
                break
            n=n.ref
        if n is not None:
            new_node = Node(data)
            new_node.ref = n.data
            n.ref = new_node

    def remove(self, data, x):
        n=self.head
        while n.ref is not None:
            if x==n.data:
                break
            n=n.ref
        if n is not None:
            new_node = Node(data)
            new_node.ref = n.data
            n.ref = new_node.ref.ref

ll=Linked()
ll.addbegin(20)
# ll.addbegin()








