class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def Display(self):
        disp = []
        cur = self.head
        disp.append(cur.data)

        while cur.next != None:
            cur = cur.next
            disp.append(cur.data)
        print(disp)

obj = Linkedlist()
obj.head = Node(1)
element2 = Node(2)
element3 = Node(3)

obj.head.next = element2
element2.next = element3

obj.Display()

# obj = Linkedlist()
# obj.head = Node(1)
# obj2 = Linkedlist()
# obj2.head = Node(1)
# obj3 = Linkedlist()
# obj3.head = Node(1)

# obj.head.next = obj2.head
# obj2.head.next = obj3.head

# obj.Display()