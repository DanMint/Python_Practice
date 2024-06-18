class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


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
        


queue1 = Queue(1)

queue1.insert(6)
queue1.insert(5)
queue1.insert(4)
queue1.insert(3)
queue1.insert(2)
queue1.insert(1)
queue1.top()
queue1.pop()
queue1.top()
queue1.pop()
queue1.top()
queue1.pop()
queue1.top()
queue1.pop()
queue1.top()
queue1.pop()
queue1.top()
queue1.pop()
queue1.top()

queue1.pop()