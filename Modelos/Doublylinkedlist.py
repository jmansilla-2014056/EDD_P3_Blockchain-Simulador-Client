class Node:
    def __init__(self, data, hash):
        self.item = data
        self.hash = None
        self.prev = None
        self.pref = None
        self.hash = hash


class DoublyLinkedList:
    def __init__(self):
        self.start_prev = None
        self.start_node = None

    def insert_in_emptylist(self, data, hash):
        if self.start_node is None:
            new_node = Node(data, hash)
            self.start_node = new_node
        else:
            print()

    def insert_at_start(self, data, hash):
        if self.start_node is None:
            new_node = Node(data, hash)
            self.start_node = new_node
            return
        new_node = Node(data, hash)
        new_node.prev = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data, hash):
        if self.start_node is None:
            new_node = Node(data, hash)
            self.start_node = new_node
            return
        n = self.start_node
        while n.prev is not None:
            n = n.prev
        new_node = Node(data, hash)
        n.prev = new_node
        new_node.pref = n

    def delete_at_start(self):
        if self.start_node is None:
            return
        if self.start_node.prev is None:
            self.start_node = None
            return
        self.start_node = self.start_node.prev

    def delete_at_end(self):
        if self.start_node is None:
            return
        if self.start_node.prev is None:
            self.start_node = None
            return
        n = self.start_node
        while n.prev is not None:
            n = n.prev
        n.pref.prev = None

    def count(self):
        x = 0
        if self.start_node is None:
            print()
        else:
            n = self.start_node
            while n is not None:
                x += 1
                n = n.prev
        return x
