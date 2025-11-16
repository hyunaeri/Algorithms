# 백준 2217
# 실버 4
# https://www.acmicpc.net/problem/2217

import sys
read = sys.stdin.readline

if __name__ == '__main__':
  
  # 로프 개수
  N = int(read())
  
  # 각 로프 정보
  rope_info = [ int(read()) for _ in range(N) ]
  rope_info.sort(key = lambda x: x)
  
  # for rope in rope_info:
  #   print(rope)
  
  # 로프를 사용해서 들어올릴 수 있는 최대 중량
  answer = []
  
  for rope in rope_info:
    answer.append(rope * N)
    N -= 1
  
  print(max(answer))