# 백준 1194 달이 차오른다, 가자
# 비트 마스크
import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def haveKey(cur_key, door):
    # and 연산 결과 거짓이면 0을 리턴함.
    value = cur_key & (1 << (ord(door) - ord('A')))
    return True if value else False

def BFS(x,y):
    # 초기 상태는 x,y 좌표와 키를 하나도 가지고 있지 않으므로 0을 담아줌
    queue = deque()
    queue.append([x,y,0])

    visited = [[[-1] * (1 << 6) for _ in range(M)] for _ in range(N)]
    visited[x][y][0] = 0

    while queue:
        x,y,key = queue.popleft()
        # 출구에 도착하면 최소 비용 리턴
        if maze[x][y] == '1':
            return visited[x][y][key]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][key] == -1:
                # 방문한 지역이 빈칸이거나 출구 도달시
                if maze[nx][ny] == '.' or maze[nx][ny] == '1':
                    visited[nx][ny][key] = visited[x][y][key] + 1
                    queue.append([nx,ny,key])
                # 열쇠가 있는 칸에 방문   
                elif 'a' <= maze[nx][ny] <= 'f':
                    temp = key | (1 << (ord(maze[nx][ny]) - ord('a')))
                    visited[nx][ny][temp] = visited[x][y][key] + 1
                    queue.append([nx,ny,temp])
                # 문이 있는 칸에 방문
                elif 'A' <= maze[nx][ny] <= 'F':
                    # 키를 가지고 있다면
                    if haveKey(key, maze[nx][ny]):
                        visited[nx][ny][key] = visited[x][y][key] + 1
                        queue.append([nx,ny,key])

    # 다 돌았는데 출구에 도달하지 못한다면
    return -1



if __name__ == '__main__' :
    # 미로의 세로, 가로 크기
    N,M = map(int,read().split())
    maze = [ list(map(str,read().rstrip())) for _ in range(N) ]

    for i in range(N):
        for j in range(M):
            # 민식이의 초기 위치
            if maze[i][j] == '0':
                start_x, start_y = i,j
                maze[i][j] = '.'

    print(BFS(start_x,start_y))          