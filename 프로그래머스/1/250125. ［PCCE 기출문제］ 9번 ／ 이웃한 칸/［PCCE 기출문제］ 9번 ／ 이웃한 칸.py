# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(board, h, w):
    answer = 0
    check_color = board[h][w]
    
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        
        # 보드의 범위를 벗어나는 경우
        if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board) :
            continue
            
        if board[nx][ny] == check_color :
            answer += 1
        
    return answer