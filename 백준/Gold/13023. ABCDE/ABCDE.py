# 백준 13023 ABCDE
import sys
read = sys.stdin.readline

# 사람의 수, 친구 관계의 수
N,M = map(int,read().split())
friends = [ [] for _ in range(N) ]
visited = [False] * N
answer = False

for _ in range(M):
    a, b = map(int, read().split())
    friends[a].append(b)
    friends[b].append(a)

def dfs(start, count):
    global answer

    if count == 4:
        answer = True
        return
    
    for next_friend in friends[start]:
        if not visited[next_friend]:
            visited[next_friend] = True
            dfs(next_friend, count + 1)
            visited[next_friend] = False

for i in range(N):
    # 초기 방문 등록
    visited[i] = True
    # 친구 관계 탐색
    dfs(i,0)
    # 초기 방문 해제
    visited[i] = False
    # 친구 관계가 존재한다면
    if answer:
        break

if answer:
    print(1)
else:
    print(0)
