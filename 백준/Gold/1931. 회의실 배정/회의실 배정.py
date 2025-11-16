# 백준 1931
# 골드 5
# https://www.acmicpc.net/problem/1931

import sys
read = sys.stdin.readline

if __name__ =='__main__':
  answer = 0
  
  # 회의의 수
  N = int(read())
  
  # 회의 정보
  conf_info = []
  
  for _ in range(N):
    start, end = map(int, read().split())
    conf_info.append((start, end))
  
  # 먼저 끝나는 회의 순으로 정렬
  conf_info.sort(key = lambda x: (x[1], x[0]))
  
  # for conf in conf_info:
  #   print(conf)
  
  current_date = -1
  
  for conf_start, conf_end in conf_info:
    if current_date > conf_start:
      continue

    answer += 1
    current_date = conf_end

  print(answer)
