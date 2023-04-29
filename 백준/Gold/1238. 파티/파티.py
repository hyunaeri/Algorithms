# 백준 1238 파티
import sys
import heapq
read = sys.stdin.readline
INF = int(1e9)

# N개의 마을(= N개의 노드), M개의 도로 개수(= M개의 간선), 만나는 마을 X
N,M,X = map(int,read().split())
graph = [ [] for _ in range(N+1) ]

for _ in range(M):
    start, end, time = map(int, read().split())
    graph[start].append([end,time])

# print(graph)

def dijkstra(start):
    queue = []
    distance = [INF] * (N+1)

    # 자기 자신으로 가는 비용은 0
    distance[start] = 0
    heapq.heappush(queue, [0,start])

    while queue:
        # 비용, 현재 노드
        dist, current_node = heapq.heappop(queue)

        if distance[current_node] < dist:
            continue

        for next_node, next_cost in graph[current_node]:
            cost = dist + next_cost

            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(queue, [cost, next_node])

    return distance


result = 0
for i in range(1, N + 1):
    go = dijkstra(i)
    back = dijkstra(X)
    result = max(result, go[X] + back[i])

print(result)