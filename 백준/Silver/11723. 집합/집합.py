# 백준 11723 집합
import sys
read = sys.stdin.readline

M = int(read())
all_num = [i for i in range(1,21)]
result = set()

for _ in range(M):
    command = read().rstrip().split()

    if len(command) == 1:
        if command[0] == 'all':
            result.update(all_num)
        
        elif command[0] == 'empty':
            result.clear()

    else:
        order, num = command[0], command[1]
        num = int(num)

        if order == 'add':
            result.add(num)

        elif order == 'remove':
            result.discard(num)

        elif order == 'check':
            if num in result:
                print("1")
            else:
                print("0")

        elif order == 'toggle':
            if num in result:
                result.discard(num)
            else:
                result.add(num)