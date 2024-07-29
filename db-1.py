class node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class ll:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end= "")
                n = n.ref

    def add_first(self, data):
        new_node = node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            else:
                n = n.ref
        if n is None:
            print("Given node", x ," is not present in LL")
        else:
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            print("LL is not empty")

    def delete_begin(self):
        if self.head is None:
            print("LL is empty, so we can't perform delete operation")
        else:
            self.head = self.head.ref

    def delete_end(self):
        n = self.head
        if self.head is None:
            print("LL is empty, so we can't perform delete operation")
        while n.ref.ref is not None:
            n = n.ref
        if n.ref.ref is None:
            n.ref = None

    def delete_by_value(self, x):
        n = self.head
        if self.head is None:
            print("LL is empty, so we can't perform delete operation")
            return
        if x == n.data:
            ll.delete_begin(self)
            return
        while n.ref is not None:
            if x == n.ref.data:
                break
            else:
                n = n.ref
        if n.ref is None:
            print("Node is not present in ll, so we can't perform delete operation")
        else:
            n.ref = n.ref.ref



m = ll()
m.insert_empty(3939393)
m.add_first(1)
list1 = [22,12,13,42,445,2829,2,29123]
for i in list1:
    m.add_end(i)
m.add_after(200,32)
m.delete_by_value(42)
m.print_ll()