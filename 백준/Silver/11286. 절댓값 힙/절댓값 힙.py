# 2025.05.15 (목)
# 백준 11286 절댓값 힙
# 실버 1

import heapq
import sys
read = sys.stdin.readline

# 연산의 개수
N = int(read())

heap = []
heapq.heapify(heap)

for _ in range(N):
  command = int(read())
  
  if command != 0:
    abs_command = abs(command)
    heapq.heappush(heap, (abs_command, command))
    
  else:
    if len(heap) == 0:
      print(0)
    else:
      result = heapq.heappop(heap)
      print(result[-1])