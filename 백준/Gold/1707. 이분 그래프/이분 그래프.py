# 백준 1707 이분그래프
# 이분그래프 : 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프
import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

# 테스트 케이스 수
T = int(read())

def dfs(x):
    global result
    
    for node in graph[x]:
        # 인접한 노드에 색칠이 되어 있지 않다면
        if visited[node] == 0:
            # 현재 노드의 반대 색으로 칠해준다
            if visited[x] == 1:
                visited[node] = 2
            elif visited[x] == 2:
                visited[node] = 1
            dfs(node)

        # 이웃한 노드가 색칠이 되어 있다면
        else:
            # 현재 노드와 동일한 색으로 칠해져 있다면, 이분그래프가 아님
            if visited[node] == visited[x]:
                result = False
                return

for _ in range(T):
    # 정점의 개수, 간선의 개수
    v,e = map(int, read().rstrip().split())
    graph = [ [] for _ in range(v+1) ]
    visited = [0] * (v+1)

    for _ in range(e):
        x,y = map(int, read().rstrip().split())
        graph[x].append(y)
        graph[y].append(x)

    # 이분 그래프 여부
    result = True

    # 모든 노드 탐색
    for i in range(1,v+1):
        # 색칠이 되어 있지 않다면
        if visited[i] == 0:
            # i 노드를 1로 색칠
            visited[i] = 1
            # 다른 이웃한 노드들에 대해서 색칠
            dfs(i)
            # 현재 i 노드로부터 이분 그래프가 아니라는 것을 발견
            if result == False:
                break
    
    # 이분 그래프가 아니라면
    if result == False:
        print("NO")
    else:
        print("YES")