# 백준 1475 방 번호
import sys
read = sys.stdin.readline

# 0~9 필요한 갯수
num_cnt = [0] * 10

# 다솜이의 방 번호
N = list(read().rstrip())

for num in N:
    if num == '6' or num == '9':
        if num_cnt[6] <= num_cnt[9]:
            num_cnt[6] += 1
        else:
            num_cnt[9] += 1
    
    else:
        num_cnt[int(num)] += 1

print(max(num_cnt))
