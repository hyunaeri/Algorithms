# 백준 11967 불켜기
import sys
from collections import deque, defaultdict
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N, M = map(int,read().split())

# False : 불이 꺼져있음.
# True : 불이 켜져있음.
room = [ [False]*N for _ in range(N) ]
room[0][0] = True

# 방문 배열
visited = [ [False]*N for _ in range(N) ]

# Default 값으로 리스트를 줌.
# key에 해당하는 value를 지정해주지 않으면 빈 리스트로 초기화 됨.
switch = defaultdict(list)

def bfs():
    # 불을 켤수 있는 방의 개수
    cnt = 1
    q = deque()
    q.append((0,0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        # 그 방에서 다른방에 불을 켤 수 있다면
        for light_x, light_y in switch[(x,y)]:
            if not room[light_x][light_y]:
                # 불 켜기
                room[light_x][light_y] = True
                cnt += 1
                for i in range(4):
                    nx,ny = light_x + dx[i], light_y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if visited[nx][ny]:
                            q.append((nx,ny))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 이동한 방이 불이 켜져 있다면
                if room[nx][ny] and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = True

    return cnt

for _ in range(M):
    # (x,y)방에서 (a,b)방의 불을 켜고 끌 수 있음.
    x,y,a,b = map(int,read().split())
    switch[(x-1,y-1)].append((a-1, b-1))

print(bfs())