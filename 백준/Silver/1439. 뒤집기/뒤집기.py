import sys
read = sys.stdin.readline

s = read().rstrip()

pairWithZero = 1 if s[0] == '0' else 0
pairWithOne = 1 if s[0] == '1' else 0

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0':
            pairWithZero += 1
        else:
            pairWithOne += 1

print(min(pairWithZero, pairWithOne))