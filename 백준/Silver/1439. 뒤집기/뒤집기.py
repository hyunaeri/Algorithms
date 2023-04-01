# 백준 1439 뒤집기
import sys
read = sys.stdin.readline

S = read().rstrip()

# 0과 1로 이루어진 그룹의 수
cnt_0 = 0
cnt_1 = 0

# 기준 문자
check = S[0]
if check == '0':
    cnt_0 += 1
elif check == '1':
    cnt_1 += 1

for i in range(1, len(S)):
    if S[i] != check:
        if S[i] == '0':
            cnt_0 += 1
        else:
            cnt_1 += 1
        check = S[i]

print(min(cnt_0,cnt_1))


