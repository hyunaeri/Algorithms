# 백준 15650 N과 M 2
import sys
read = sys.stdin.readline

# 1~N 까지의 자연수 중 중복없이 M개를 선택한 수열
# 수열은 오름차순이어야 된다.
N,M = map(int,read().split())

visited = [False for _ in range(N+1)] 
result = [0]

def DFS():
    # 종료 조건
    if len(result) == M+1:
        print(*result[1:], sep = ' ')
        return
    
    for i in range(1, N+1):
        if not visited[i] and result[-1] < i:
            visited[i] = True
            result.append(i)
            DFS()
            result.pop()
            visited[i] = False

DFS()
