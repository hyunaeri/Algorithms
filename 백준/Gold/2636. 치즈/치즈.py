# 백준 2636 치즈
import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 세로, 가로 길이
N,M = map(int, read().split())
# 치즈판 업데이트
cheese = [ list(map(int,read().split())) for _ in range(N) ]
result = 0
prev = 0

def melting_cheese():
    global result, prev
    result += 1

    queue = deque()
    queue.append((0,0))
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True

    # 녹을 예정인 치즈 위치 들을 담음
    melting_list = []

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 현재 위치 공기 -> 네 방향 중 한 방향으로 이동했는데, 미 방문인 치즈를 만났다
                if cheese[nx][ny] == 1:
                    melting_list.append([nx,ny])
                # 이동한 위치도 공기
                elif cheese[nx][ny] == 0:
                    queue.append([nx,ny])
                
                visited[nx][ny] = True
    
    # 이번 탐색에서 녹일 치즈가 있다면
    if len(melting_list) != 0:
        for x, y in melting_list:
            cheese[x][y] = 0
        return len(melting_list)
    
    else:
        # 이전 탐색에서 치즈가 모두 녹았기 때문에 -1
        print(result - 1)
        print(prev)
        return 0
        
while True:
    prev = melting_cheese()

    if prev == 0:
        break