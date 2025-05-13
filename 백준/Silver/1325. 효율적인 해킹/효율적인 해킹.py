# 2025.05.13 (화)
# 백준 1325 효율적인 해킹
# 실버 1

from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().split())

trust = [[] for _ in range(N + 1)]

# b가 a를 신뢰 → b를 해킹하면 a도 해킹 가능
for _ in range(M):
    a, b = map(int, read().split())
    trust[b].append(a)

def bfs(start):
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque([start])
    cnt = 1

    while q:
        cur = q.popleft()
        for nxt in trust[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                cnt += 1
                q.append(nxt)
    return cnt

result = [0] * (N + 1)

for i in range(1, N + 1):
    result[i] = bfs(i)
    
max_cnt = max(result)

for i in range(1, N + 1):
    if result[i] == max_cnt:
        print(i, end=' ')
