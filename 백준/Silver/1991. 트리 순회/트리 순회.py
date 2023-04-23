# 백준 1991 트리 순회
import sys
read = sys.stdin.readline

# 이진트리의 노드 개수
n = int(read())
tree = dict()

for _ in range(n):
    root, left, right = map(str, read().rstrip().split())
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end = '')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')