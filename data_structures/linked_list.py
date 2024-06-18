class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    head = None
    current = None
    amount_created = 0

    def __init__(self, val):
        temp = Node()
        temp.val = val
        self.head = temp
        self.current = self.head
        self.amount_of_linked_lists()

    @classmethod
    def amount_of_linked_lists(cls):
        cls.amount_created += 1

    @classmethod
    def dipslay_amount_of_linkedlists(cls):
        print(cls.amount_created)

    def add_value(self, val):
        temp = Node()
        temp.val = val
        temp.prev = self.current
        self.current.next = temp
        self.current = temp

    def display_linked_list(self):
        temp = self.head

        while temp.next != None:
            print(temp.val)
            temp = temp.next


list1 = LinkedList(1)
list1.add_value(2)
list1.add_value(3)
list1.add_value(4)
list1.add_value(5)
list1.add_value(6)
list1.add_value(7)

list1.display_linked_list()

