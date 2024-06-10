class node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = node(1)           #first node
print(node1.data)


class list:

    #adding nodes to linkedlist
    def add_nodes(self, data):
        self.new_node = node(data)
        self.current = node1
        while self.current.next is not None:
            self.current = self.current.next

        self.current.next = self.new_node
        print("")
        self.current = node1
        while self.current is not None:
            print(self.current.data, end="->")
            self.current = self.current.next
        print("none")


    # insertion at begin
    def insert_at_begin(self, data):
        self.new_node = node(data)
        self.current = node1

        self.head = node1
        if self.head is None:
            self.head = self.new_node
        else:
            self.new_node.next = self.head
            self.head = self.new_node

        print("")
        print("after adding at start")

        self.current = self.head
        while self.current is not None:
            print(self.current.data, end="->")
            self.current = self.current.next
        print("none")


    #insertion at end
    def insert_at_end(self, data):
        self.new_node = node(data)
        self.current = node1
        while self.current.next is not None:
            self.current = self.current.next

        self.current.next = self.new_node
        print("")
        print("after adding at end")
        self.current = self.head
        while self.current is not None:
            print(self.current.data, end="->")
            self.current = self.current.next
        print("none")


    # insertion at specific index
    def insert_at_index(self, data, index):
        self.new_node = node(data)
        self.pos = 0
        self.current = node1

        if self.pos == index:
            self.insert_at_begin(data)
        else:
            while self.current != None and self.pos + 1 != index:
                self.pos = self.pos + 1
                self.current = self.current.next

            if self.current != None:
                self.new_node.next = self.current.next
                self.current.next = self.new_node
            else:
                print("no index present")

        print("")
        print("after adding at specific position(2)")

        self.current = self.head
        while self.current is not None:
            print(self.current.data, end="->")
            self.current = self.current.next
        print("none")


    # removing /deleting last node
    def remove_at_end(self):
        current = self.head
        while current.next.next != None:
            current = current.next

        current.next = None

        print("")
        print("after removing last node")

        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("none")

    # removing/deleting first node
    def remove_at_begin(self):
        self.head = self.head.next

        print("")
        print("after removing first node")

        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("none")

    # removing specific index node
    def remove_at_pos(self, index):
        self.pos = 0
        self.current = self.head
        if self.pos == index:
            self.head = self.current.next.head
        else:
            while self.current != None and self.pos + 1 != index:
                self.pos = self.pos + 1
                self.current = self.current.next

            if self.current!=None:
                self.current.next=self.current.next.next
            else:
                print("none")


        print("")
        print("after removing specific index node")

        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("none")

#adding nodes to list
list1 = list()
list1.add_nodes(2)
list1.add_nodes(3)
list1.add_nodes(4)
list1.add_nodes(5)

#printing original list
print("")
print("original linklist")
current = node1
while current is not None:
    print(current.data, end="->")
    current = current.next
print("none")

#operations on list
list1.insert_at_begin(6)
list1.remove_at_begin()

list1.insert_at_end(7)
list1.remove_at_end()

list1.insert_at_index(100, 2)
list1.remove_at_pos(2)
