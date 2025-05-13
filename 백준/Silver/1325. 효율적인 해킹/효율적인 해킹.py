# 백준 1325 효율적인 해킹
# https://www.acmicpc.net/problem/1325

from collections import deque
import sys
read = sys.stdin.readline

# 컴퓨터의 수, 관계 수
N,M = map(int,read().split())

computer = [ [] for _ in range(N+1) ]

# a 가 b 를 신뢰한다.
for _ in range(M):
    trust_a, trust_b = map(int, read().split())
    computer[trust_b].append(trust_a)
    

# print(computer)

def bfs(x):
    visited = [False] * (N+1)
    q = deque()
    q.append(x)
    visited[x] = True
    count = 1
    
    while q:
        comp = q.popleft()
        
        for com in computer[comp]:
            if not visited[com]:
                q.append(com)
                count += 1
                visited[com] = True
    
    return count

max_cnt = 1
answer = []
for i in range(1, N+1):
    temp_cnt = bfs(i)
    
    if temp_cnt > max_cnt:
        max_cnt = temp_cnt
        answer = []
        answer.append(i)
        
    elif temp_cnt == max_cnt:
        answer.append(i)
    
print(*answer)