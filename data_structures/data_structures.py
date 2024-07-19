import random

# Implement node
class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

#STACK

class Stack:
    def __init__(self, val = -12345678):
        temp = Node(val)
        self.head = temp
        self.current = self.head
    
    def insert(self, val):
        temp = Node(val)

        if self.head == None:
            self.head = temp
            self.current = self.head
            return
        
        temp.prev = self.current
        self.current = temp


    def pop(self):
        if self.current == None:
            raise ValueError("Cant pop an empty stack")
        
        temp = self.current
        self.current = None
        self.current = temp.prev

    def output_stack(self):
        temp = self.current

        while temp != None:
            print(temp.val)
            temp = temp.prev

#QUEUE

class Queue:
    def __init__(self, value):
        temp = Node(value)
        self.head = temp
        self.current = self.head

    def insert(self, val):
        temp = Node(val)
        
        if self.head == None:
            self.head = temp
            self.current = self.head
            return


        self.current.next = temp  
        self.current = temp


    def pop(self):
        if self.head == None:
            raise ValueError("Cant pop an empty queue")
        
        temp = self.head
        self.head = None
        self.head = temp.next



    def top(self):
        print(self.head.val)
        



# Doubely linked list

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


# Hash Tabels

class LinkedList:
    head = None
    current = None

    def __init__(self, val):
        temp = Node()
        temp.val = val
        self.head = temp
        self.current = self.head

  
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


class HashMap:

    def __init__(self, size):
        self.hash_table = [None,] * size
        self.hash_table_size = size
        self.collisions = [0,] * size

    @staticmethod
    def hash_function(val, size):
        return val % size
    
    def add_value(self, val):
        pos = HashMap.hash_function(val, self.hash_table_size)

        if self.hash_table[pos] == None:
            self.hash_table[pos] = LinkedList(val)
        else:
            self.hash_table[pos].add_value(val)
            self.collisions[pos] += 1

    def get_number_of_collisions(self):
        for i in range(0, len(self.collisions)):
            print("position ", i ," has ", self.collisions[i], " collisions")


stack1 = Stack(1)
stack1.insert(2)
stack1.insert(3)
stack1.output_stack()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
