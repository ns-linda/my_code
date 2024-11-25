class Node:
    def __init__(self, data):
        self.data= data
        self.ref = None

class Linked:
    def __init__(self):
        self.head = None

    def pprint(self):
        n=self.head
        if n is None:
            print("empty list")
        else:
            while n is not None:
                print(n.data)
                n=n.ref

    def addbegin(self, data):
        if self.head is None:
            self.head=Node(data)
        else:
            new_node= Node(data)
            new_node.ref=self.head  ## begin should self.head
            self.head=new_node

    def addend(self, data):
        n=self.head
        while n.ref is not None:
            n=n.ref
        new_node= Node(data)
        new_node.ref=n.ref  ## end should be n.ref
        n.ref=new_node

    def addmiddile(self, data, x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        new_node = Node(data)
        new_node.ref = n.ref  ## end should be n.ref
        n.ref = new_node

    def remove(self, x):
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        n.ref=n.ref.ref

ll=Linked()
ll.addbegin(30)
ll.addbegin(20)
ll.addbegin(10)
ll.addmiddile(40,30)
ll.addend(50)
ll.addend(60)
ll.remove(20)
ll.pprint()
