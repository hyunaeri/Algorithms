# 백준 17071
# 플래티넘 5
# https://www.acmicpc.net/problem/17071

from collections import deque
import sys
read = sys.stdin.readline

MAX = 500000

def solution(start, K0):  
  q = deque([start])
  visited = [ [False] * (MAX + 1) for _ in range(2) ]
  visited[0][start] = True
  time = 0
  
  while True:
    # time 초의 동생 위치
    K = K0 + (time * (time + 1) // 2)
    
    if K > MAX:
      return -1
    
    # 이미 방문한적이 있는 좌표면 (2초 간격으로 제자리로 돌아올 수 있음)
    if visited[time % 2][K]:
      return time
    
    time += 1
    
    for _ in range(len(q)):
      current = q.popleft()
      
      for next in [current - 1, current + 1, 2 * current]:
        if 0 <= next < MAX + 1 and not visited[time % 2][next]:
          visited[time % 2][next] = True
          q.append(next)

if __name__ == '__main__':
  
  # 수빈, 동생 위치
  N, K = map(int, read().rstrip().split())
  
  print(solution(N, K))
