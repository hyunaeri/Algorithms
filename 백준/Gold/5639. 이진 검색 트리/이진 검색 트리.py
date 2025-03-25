import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, data):
        current_node = self
        while True:
            if data < current_node.value:
                if current_node.left is None:
                    current_node.left = BinaryTree(data)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BinaryTree(data)
                    break
                else:
                    current_node = current_node.right

    def printPostOrder(self):
        if self.left is not None:
            self.left.printPostOrder()
        if self.right is not None:
            self.right.printPostOrder()
        print(self.value)

tree = BinaryTree(int(read()))

while True:
    try:
        tree.insert(int(read()))
    except:
        break
      
tree.printPostOrder()