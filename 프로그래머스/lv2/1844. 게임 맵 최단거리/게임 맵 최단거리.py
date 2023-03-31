from collections import deque

def solution(maps):
    def bfs(a,b):
        queue = deque()
        queue.append((a,b))
    
        while queue:
            x,y = queue.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx = x + dx
                ny = y + dy
            
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    queue.append((nx,ny))
                    maps[nx][ny] = maps[x][y] + 1
    
    
    n = len(maps)
    m = len(maps[0])
    
    bfs(0,0)
    answer = maps[n-1][m-1]
    
    if answer == 1:
        return -1
    
    return answer