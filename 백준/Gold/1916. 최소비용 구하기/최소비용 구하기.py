# 백준 1916 최소비용 구하기
# 골드 5

import heapq
import sys
read = sys.stdin.readline

def dijkstra(startPoint, priorityQueue, distance):
  distance[startPoint] = 0
  heapq.heappush(priorityQueue, (0, startPoint))
  
  while priorityQueue:
    cost, currentPoint = heapq.heappop(priorityQueue)
    
    if distance[currentPoint] < cost:
      continue
    
    for nextPoint, nextCost in bus[currentPoint]:
      totalCost = cost + nextCost
      if totalCost < distance[nextPoint]:
        distance[nextPoint] = totalCost
        heapq.heappush(priorityQueue, (totalCost, nextPoint))

N = int(read())
M = int(read())

bus = [ [] for _ in range(N+1) ]

for _ in range(M):
  start, end, cost = map(int, read().split())
  bus[start].append((end, cost))

startPoint, endPoint = map(int, read().split())
distance = [float('inf')] * (N+1)
priorityQueue = []

dijkstra(startPoint, priorityQueue, distance)
print(distance[endPoint])