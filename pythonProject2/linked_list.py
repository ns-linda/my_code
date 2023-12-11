class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linked_list:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_after(self,data,x):
        n= self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("value is not present")
        else:
            new_node=Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref = new_node




l_l = Linked_list()
l_l.add_begin(10)
l_l.add_after(15,10)
l_l.add_begin(20)
l_l.add_end(100)
l_l.print_ll()