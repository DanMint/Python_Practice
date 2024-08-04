# in a BST always the left child is ALWAYS less then the parent and the right child is ALWAYS GREATER OR EUAL TO its parent

class BST:
    def __init__(self, value = None) -> None:
        self.root = self.__Node(value)
        self.root.next = None
        self.root.parent = None
        if value is None:
            self.node_amout = 0
        else:
            self.node_amout = 1

    class __Node:
        def __init__(self, value = None) -> None:
            self.val = value
            self.right = None
            self.left = None
            self.parent = None

    def insert(self, value) -> None:
        temp = self.__Node(value)
        current = self.root

        if current.val == None:
            current.val = value
            return
        
        while True:
            if value >= current.val:
                if current.right == None:
                    temp.parent = current
                    current.right = self.__Node(value)
                    return
                else:
                    current = current.right
            
            else:
                if current.left == None:
                    temp.parent = current
                    current.left = self.__Node(value)
                    return
                else:
                    current = current.left

    def inorder_tree_walk(self, current):
        if current == None:
            return
        self.inorder_tree_walk(current.left)
        print(current.val, end=" ")
        self.inorder_tree_walk(current.right)

    def tree_search(self, current, target) -> __Node:
        if current == None or target == current.val:
            return current
        
        if target >= current.val:
            self.tree_search(current.right, target)
            
        else:
            self.tree_search(current.left, target)

    @property
    def max(self) -> int:
        current = self.root
        
        while True:
            if current.right == None:
                print(current.val)
                return
            
            current = current.right

    @property
    def min(self) -> int:
        current = self.root

        while True:
            if current.left == None:
                print(current.val)
                return 
            
            current = current.left

    @property
    def print(self):
        return self.inorder_tree_walk(self.root)

tree1 = BST(5)
tree1.insert(1)
tree1.insert(4)
tree1.insert(0)
tree1.insert(10)
tree1.insert(8)
tree1.insert(3)
tree1.insert(5)

tree1.min


