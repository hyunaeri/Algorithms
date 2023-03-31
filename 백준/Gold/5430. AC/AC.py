# 백준 5430 AC
from collections import deque
import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    flag = 1
    reverse_cnt = 0
    # 첫 줄에는 수행할 함수
    command = list(read().rstrip())
    # 다음 줄에는 배열에 들어 있는 수의 개수
    num_cnt = int(read().rstrip())
    # 마지막 줄에는 배열에 들어 있는 정수
    num = read().rstrip()
    queue = deque(num[1:-1].split(','))

    if num_cnt == 0:
        queue = deque()

    for i in range(len(command)):
        if command[i] == 'R':
            reverse_cnt += 1
        elif command[i] == 'D':
            if len(queue) == 0:
                flag = 0
                print('error')
                break
            else:
                if reverse_cnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if flag == 0:
        continue

    else:
        if reverse_cnt % 2 == 1:
            queue.reverse()
            print('['+ ','.join(queue) + ']')
        else:
            print('['+ ','.join(queue) + ']')
    