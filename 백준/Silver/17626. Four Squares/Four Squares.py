import sys

n = int(sys.stdin.readline().strip())

# dp[i]: i개의 제곱수로 만들 수 있는 숫자 리스트
dp = [set() for _ in range(5)]
dp[0].add(0)  # 0은 아무것도 더하지 않는 경우

# n 이하의 모든 제곱수를 구함
squares = []
i = 1
while i * i <= n:
    squares.append(i * i)
    i += 1

# DP 진행
for count in range(1, 5):  # 최대 4개의 제곱수까지 가능
    for num in dp[count - 1]:  # 이전 단계에서 만든 숫자들 확인
        for square in squares:
            new_num = num + square
            if new_num > n:  # 초과하면 스킵
                break
            dp[count].add(new_num)
    if n in dp[count]:  # n이 만들어지면 종료
        print(count)
        sys.exit()