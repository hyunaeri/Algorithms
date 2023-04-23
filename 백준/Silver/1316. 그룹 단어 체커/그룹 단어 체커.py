# 백준 1316 그룹 단어 체커

import sys

test_case = int(sys.stdin.readline())
result = test_case

for _ in range(test_case):
  word = sys.stdin.readline().rstrip()
  for i in range(len(word) - 1):
    if (word[i] != word[i + 1]):
      if (word[i] in word[i + 1:]):
        result -= 1
        break

print(result)
