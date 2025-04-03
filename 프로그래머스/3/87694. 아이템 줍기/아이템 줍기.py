from collections import deque

def bfs(board, start_x, start_y, target_x, target_y):
    q = deque([(start_x, start_y, 0)])
    
    visited = [ [False] * 102 for _ in range(102) ]
    visited[start_x][start_y] = True
    
    while q:
        x, y, dist = q.popleft()
        
        if x == target_x and y == target_y:
            return dist
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 1 <= nx < 101 and 1 <= ny < 101:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
        

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 각 직사각형을 나타내는 모든 좌표값은 1 이상 50 이하이나, 2배로 늘려서 받기
    board = [ [0] * 102 for _ in range(102) ]
    
    for rec in rectangle:
        # map(func, iterable)
        x1, y1, x2, y2 = map(lambda x: x*2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # 직사각형 내부의 값은 2로 설정
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 2
                # 테두리
                else:
                    # 다른 직사각형의 내부가 아닌 경우
                    if board[i][j] != 2:
                        board[i][j] = 1
                        
                        
    answer = bfs(board, characterX * 2, characterY * 2, itemX * 2, itemY * 2) / 2
    return answer