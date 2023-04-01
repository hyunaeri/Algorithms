import sys
s = list(map(int, sys.stdin.readline().strip()))

cnt = 0
# 반복문을 통해 문자열을 확인
for i in range(len(s) - 1):
    # 현재 문자와 다음 문자가 다르면 카운트
    if s[i] != s[i + 1]:
        cnt += 1

print((cnt + 1) // 2)