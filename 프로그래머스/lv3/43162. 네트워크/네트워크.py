def solution(n, computers):
    # 0 ~ n-1번 컴퓨터의 방문 여부를 담을 리스트
    visited = [False]*n 
    answer = 0
    
    def dfs(a):
        visited[a] = True
        for i in range(n):
            if not visited[i] and computers[a][i]:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer