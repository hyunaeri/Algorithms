# 백준 2675 문자열 반복

import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
  R, S = sys.stdin.readline().split()
  for str in S:
    print(str * int(R), end = '')
  print()
