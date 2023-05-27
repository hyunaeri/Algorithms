import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = []
    for i in map(int,input().split()):
        if i % 2 == 0:
            arr.append(i)
    print(sum(arr),min(arr))