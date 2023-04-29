# 백준 14938 서강 그라운드
import sys
import heapq
read = sys.stdin.readline
INF = int(2e9)

# 지역의 개수, 수색 범위, 길의 개수
v, limit, e = map(int, read().split())
items = [0] + list(map(int,read().split()))
graph = [ [] for _ in range(v+1) ]

for _ in range(e):
    a,b,length = map(int, read().split())
    graph[a].append([b, length])
    graph[b].append([a, length])

def dijkstra(start):
    queue = []
    distance = [INF]*(v+1)

    # 자기 자신으로 가는 비용은 0
    distance[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        dist, current_node = heapq.heappop(queue)

        if distance[current_node] < dist:
            continue

        for next_node, next_cost in graph[current_node]:
            cost = dist + next_cost

            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(queue, [cost, next_node])

    return distance

result = []

for i in range(1, v+1):
    temp = dijkstra(i)
    get_item = 0

    for j in range(1, v+1):
        # 수색 범위 내이면
        if temp[j] <= limit:
            get_item += items[j]
    result.append(get_item)

print(max(result))