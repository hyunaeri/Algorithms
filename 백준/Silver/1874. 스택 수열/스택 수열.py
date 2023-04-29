# 백준 1874 스택 수열
import sys
read = sys.stdin.readline

n = int(read())
target = [int(read()) for _ in range(n)]
target_idx = 0
stack = []
result = []
num = 1


while True:
    # 타겟한 수가 스택의 최상단 수보다 크면
    if len(stack) == 0 or stack[-1] < target[target_idx]:
        stack.append(num)
        num += 1
        result.append('+')

    # 타겟한 수가 스택의 최상단 수와 같으면
    elif stack[-1] == target[target_idx]:
        stack.pop()
        result.append('-')
        target_idx += 1

    # 타겟한 수가 스택의 최상단 수보다 작으면
    elif stack[-1] > target[target_idx]:
        print("NO")
        exit(0)

    # n번의 push, n번의 pop을 하므로 2*n 번
    if len(result) == 2*n:
        break

print(*result, sep='\n')