# 백준 9012 괄호
import sys
read = sys.stdin.readline

T = int(read())

def is_VPS(p):
    global stack
    check_VPS = True

    for i in range(len(p)):
        if p[i] == '(':
            stack.append('(')

        elif p[i] == ')':
            if len(stack) == 0:
                check_VPS = False
                break
            else:
                stack.pop()

    if len(stack) != 0:
        check_VPS = False

    return check_VPS

for _ in range(T):
    parenthesis = read().rstrip()
    stack = list()

    if is_VPS(parenthesis):
        print("YES")
    else:
        print("NO")