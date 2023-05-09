# 백준 1043 거짓말
import sys
read = sys.stdin.readline

# 사람의 수, 파티의 수
N,M = map(int,read().split())

# 이야기의 진실을 아는 사람의 번호
truth_nums = set(map(int,read().split()[1:]))
party_members = []

for _ in range(M):
    # party_members[i] : 파티마다 오는 사람 번호들의 집합
    party_members.append(set(map(int,read().split()[1:])))

# 진실을 아는 사람 업데이트
for _ in range(M):
    for members in party_members:
        # 두 집합에 교집합이 발생하면
        if members & truth_nums:
            # 두 집합 합침(모두가 진실을 알게됨)
            truth_nums = truth_nums.union(members)

result = 0
for members in party_members:
    if members & truth_nums:
        continue
    result += 1

print(result)