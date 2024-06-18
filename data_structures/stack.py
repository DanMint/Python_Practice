class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev = None

class Stack:
    def __init__(self, val):
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


stack1 = Stack(1)

stack1.insert(6)
stack1.insert(5)
stack1.insert(4)
stack1.insert(3)
stack1.insert(2)
stack1.insert(1)

stack1.output_stack()

stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()

stack1.output_stack()

stack1.insert(1)

stack1.output_stack()
stack1.pop()
stack1.pop()
stack1.pop()
