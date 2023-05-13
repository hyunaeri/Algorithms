# 백준 1967 트리의 지름
import sys
sys.setrecursionlimit(10001)
read = sys.stdin.readline

def dfs(root):
    for next_node, next_weight in tree[root]:
        if dp[next_node] == -1:
            dp[next_node] = dp[root] + next_weight
            dfs(next_node)

# 노드의 개수
N = int(read())
tree = [ [] for _ in range(N+1) ]

# 트리는 사이클이 없는 '무방향 그래프'
for _ in range(N-1):
    parent, child, weight = map(int,read().split())
    tree[parent].append([child,weight])
    tree[child].append([parent,weight])

# 루트노드 (1번)에서 가장 트리의 지름이 큰 곳을 찾는다.
dp = [-1] * (N+1)
dp[1] = 0
dfs(1)

# 위에서 찾은 노드에 대한 가장 트리의 지름이 큰 곳을 찾는다.
start = dp.index(max(dp))
dp = [-1] * (N+1)
dp[start] = 0
dfs(start)

print(max(dp))