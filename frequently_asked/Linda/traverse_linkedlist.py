class Node:

    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printlist(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_End(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                n= n.ref
            n.ref = new_node

    def middle(self, data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("Node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
ll= LinkedList()
ll.add_begin(10)
ll.add_End(20)
ll.middle(15,10)
print(ll.printlist())



