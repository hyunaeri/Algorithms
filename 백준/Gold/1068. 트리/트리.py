# 2025.04.11 (금)
# 백준 1068 트리
# 골드 5
import sys
read = sys.stdin.readline

# 노드의 수
n = int(read())

# 각 노드의 부모 정보
parents = list(map(int, read().split()))

# 삭제할 노드
removed = int(read())

tree = [[] for _ in range(n)]

root = -1
for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)

answer = 0

def dfs(node):
    global answer

    if node == removed:
        return

    if len(tree[node]) == 0:
        answer += 1
        return

    has_valid_child = False
    for child in tree[node]:
        if child != removed:
            has_valid_child = True
            dfs(child)

    if not has_valid_child:
        answer += 1

dfs(root)
print(answer)