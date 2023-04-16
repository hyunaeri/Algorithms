# 백준 5014 스타트링크
import sys
from collections import deque
read = sys.stdin.readline

# F : 건물의 최고층
# S : 현재 위치한 층
# G : 스타트링크가 위치한 층
F,S,G,U,D = map(int,read().split())
visited = [False] * (F+1)
count = [0] * (F+1)

def go_startlink(x):
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        x = queue.popleft()
        if x == G:
            return count[G]

        for dx in [U,-D]:
            nx = x + dx

            if 1 <= nx <= F and visited[nx] == False:
                visited[nx] = True
                queue.append(nx)
                count[nx] = count[x] + 1

    if count[G] == 0:
        return "use the stairs"

print(go_startlink(S))