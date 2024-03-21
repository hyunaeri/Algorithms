from collections import deque
import sys
read = sys.stdin.readline

# 상하좌우 이동
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(land):
    # 세로 / 가로 길이
    n, m = len(land), len(land[0])
    visited = [ [False for _ in range(m)] for _ in range(n) ]
    answer = [0 for _ in range(m)]
    
    def bfs(x, y):
        queue = deque()
        queue.append([x,y])
        visited[x][y] = True
        count = 0
        
        # bfs 마다 최소 y 좌표 / 최대 y 좌표 기억
        min_y, max_y = y, y

        while queue:
            x, y = queue.popleft()
            count += 1
            min_y = min(min_y, y)
            max_y = max(max_y, y)

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if land[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                    
        for i in range(min_y, max_y + 1):
            answer[i] += count
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)

    
    return max(answer)
    
    