# 백준 25192 인사성 밝은 곰곰이
# 리스트로 접근하면 시간초과가 뜬다...

import sys
read = sys.stdin.readline

n = int(read())
result = 0
gomgom = set()

for _ in range(n):
    command = read().rstrip()
    if command == 'ENTER':
        gomgom.clear()
    else:
        if command not in gomgom:
            result += 1
            gomgom.add(command)

print(result)