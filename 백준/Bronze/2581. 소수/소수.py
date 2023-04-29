# 백준 2581 소수

import sys


def prime_num(min, max):
  # 범위를 매개변수로 받아옴
  prime_list = list()

  for i in range(min, max + 1):
    # check가 0이면 소수
    check = 0
    if i > 1:
      for x in range(2, i):
        if i % x == 0:
          check = 1
          break
      if check == 0:
        prime_list.append(i)

  return prime_list


m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
result = prime_num(m,n)

if len(result) == 0:
  print("-1")

else:
  sum = sum(prime_num(m,n))
  min = min(prime_num(m,n))
  print("{}\n{}".format(sum,min))