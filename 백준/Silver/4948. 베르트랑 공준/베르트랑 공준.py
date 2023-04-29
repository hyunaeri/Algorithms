# 백준 4948 베르트랑 공준

import sys


def prime_num(i):
  if i == 1:
    return False

  else:
    for x in range(2, int(i**0.5) + 1):
      if (i % x == 0):
        return False
    return True


# 문제에서 제한한 범위
num_list = list(range(2, 246913))
prime_list = list()

for num in num_list:
  if prime_num(num):
    prime_list.append(num)

while (True):
  input = int(sys.stdin.readline())
  cnt = 0
  if input == 0:
    break
  for i in prime_list:
    if input < i <= 2 * input:
      cnt += 1
  print(cnt)
