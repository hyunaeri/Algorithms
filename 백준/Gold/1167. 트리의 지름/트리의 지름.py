# 백준 1167 트리의 지름
import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

def dfs(root):
    for next_node, next_weight in tree[root]:
        if dp[next_node] == -1:
            dp[next_node] = dp[root] + next_weight
            dfs(next_node)


# 정점의 개수
V = int(read())
tree = [ [] for _ in range(V+1) ]

for _ in range(V):
    info = list(map(int,read().split()))

    for i in range(1, len(info) - 1, 2):
        tree[info[0]].append([info[i],info[i+1]])

# 아무 노드에서 가장 멀리있는 노드를 구하기
dp = [-1] * (V+1)
dp[1] = 0
dfs(1)

# 위에서 구한 노드에서 가장 멀리 떨어진 노드 구하기
start = dp.index(max(dp))
dp = [-1] * (V+1)
dp[start] = 0
dfs(start)

print(max(dp))