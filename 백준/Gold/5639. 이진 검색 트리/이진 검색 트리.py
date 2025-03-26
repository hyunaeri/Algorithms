import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
          self.root = Node(data)
          
        else:
          current_node = self.root
          while True:
            if data < current_node.value:
              if current_node.left is None:
                current_node.left = Node(data)
                break
              else:
                current_node = current_node.left
            else:
              if current_node.right is None:
                current_node.right = Node(data)
                break
              else:
                current_node = current_node.right

    def printPostOrder(self, node = None):
      if node is None:
        node = self.root
      if node.left is not None:
          self.printPostOrder(node.left)
      if node.right is not None:
          self.printPostOrder(node.right)
      print(node.value)

tree = Tree()

while True:
    try:
        tree.insert(int(read()))
    except:
        break

tree.printPostOrder()