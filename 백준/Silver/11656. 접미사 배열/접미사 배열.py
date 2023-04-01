# 백준 11656 접미사 배열
import sys
read = sys.stdin.readline

S = read().rstrip()
suffix = []
for i in range(len(S)):
    suffix.append(S[i:])

print(*sorted(suffix), sep='\n')