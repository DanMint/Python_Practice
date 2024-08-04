# create binary seacrh tree and create a method called add that adds to the tree and another func to print in order
#       5
#      / \
#     3   8    
#    / \   \
#   0   4   9

class Node:
    def __init__(self, val = None) -> None:
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, val) -> None:
        self.root = Node(val)

    def add(self, value):
        current = self.root
        
        while True:
            if value >= current.val:
                if current.right != None:
                    current = current.right
                else:
                    current.right = Node(value)
                    break
            
            else:
                if current.left != None:
                    current = current.left
                else:
                    current.left = Node(value)
                    break

    def add_recus(self, current, value):
        if value >= current.val:
            if current.right == None:
                current.right = Node(value)
                return
            self.add_recus(current.right, value)
        else:
            if current.left == None:
                current.left = Node(value)
                return
            self.add_recus(current.left, value) 

    def add_via_recurssion(self, value):
        return self.add_recus(self.root, value)

    def print_inorder(self, node):
        if node == None:
            return
        self.print_inorder(node.left)
        print(node.val, end=" ")
        self.print_inorder(node.right)

    @property
    def print(self):
        return self.print_inorder(self.root)



bst = BST(5)
bst.add_via_recurssion(3)
bst.add_via_recurssion(8)
bst.add_via_recurssion(0)
bst.add_via_recurssion(4)
bst.add_via_recurssion(9)
bst.print