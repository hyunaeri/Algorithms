# 백준 16637
# 골드 3
# https://www.acmicpc.net/problem/16637

import sys
read = sys.stdin.readline

def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def dfs(idx, current_value):
    global N, answer, expression
    
    # 더 이상 계산할 피연산자가 없음
    if idx >= N:
        answer = max(answer, current_value)
        return
    
    # 괄호 없이 계산
    op = expression[idx - 1]
    next_num = int(expression[idx])
    val = calc(current_value, op, next_num)
    dfs(idx + 2, val)
    
    # 괄호 사용 (다음 연산 먼저 계산)
    if idx + 2 < N:
        num1 = int(expression[idx])
        op2 = expression[idx + 1]
        num2 = int(expression[idx + 2])
        
        parenthesis = calc(num1, op2, num2)
        val2 = calc(current_value, op, parenthesis)
        dfs(idx + 4, val2)

if __name__ == '__main__':
    
    # 수식의 길이, 수식 정보
    N = int(read())
    expression = list(read().rstrip())
    
    if N == 1:
        print(int(expression[0]))
        exit(0)
    
    answer = -float('inf')
    
    # 첫 번째 숫자를 현재 값으로 두고 DFS
    dfs(2, int(expression[0]))
    
    print(answer)