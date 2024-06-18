class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


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


hash_map = HashMap(10)

hash_map.add_value(15)
hash_map.add_value(25)
hash_map.add_value(35)

hash_map.get_number_of_collisions()