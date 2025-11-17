# 백준 17071
# 플래티넘 5
# https://www.acmicpc.net/problem/17071

from collections import deque
import sys
read = sys.stdin.readline

MAX = 500000

def solution(start, K0):
  if start == K0:
    return 0
  
  q = deque([start])
  visited = [ [0] * (MAX + 1) for _ in range(2) ]
  time = 0
  
  while True:
    # time 초의 동생 위치
    K = K0 + (time * (time + 1) // 2)
    
    if K > MAX:
      return -1
    
    if visited[time % 2][K] != 0:
      return time
    
    time += 1
    
    for _ in range(len(q)):
      current = q.popleft()
      
      for next in [current - 1, current + 1, 2 * current]:
        if 0 <= next < MAX + 1 and visited[time % 2][next] == 0:
          visited[time % 2][next] = time
          q.append(next)

if __name__ == '__main__':
  
  # 수빈, 동생 위치
  N, K = map(int, read().rstrip().split())
  
  print(solution(N, K))
