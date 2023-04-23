# 백준 9935 문자열 폭발
# 파이썬 내장함수로 풀었는데, 테스트케이스는 다 맞으나 시간초과
# 스택으로 풀자
import sys
read = sys.stdin.readline

S = read().rstrip()
explosion_str = read().rstrip()
length = len(explosion_str)
stack = list()

for i in range(len(S)):
    stack.append(S[i])
    if stack[-length:] == list(explosion_str):
        for _ in range(length):
            stack.pop()

if stack:
    print(*stack, sep='')
else:
    print("FRULA")
