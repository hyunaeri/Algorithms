# 백준 12851 숨바꼭질 2
import sys
from collections import deque
read = sys.stdin.readline

def bfs(x):
    global cnt

    q = deque()
    q.append(x)
    visited[x] = 0

    while q:
        x = q.popleft()

        if x == K:
            cnt += 1
            continue
        
        for nx in [x-1, x+1, 2*x]:
            if 0 <= nx < 100001:
                if visited[nx] == visited[x] + 1 or visited[nx] == -1:
                    q.append(nx)
                    visited[nx] = visited[x] + 1

# 수빈이의 위치, 동생이 있는 위치
N, K = map(int,read().split())
visited = [-1] * 100001
cnt = 0

# bfs
bfs(N)

print(visited[K])
print(cnt)