import sys

input = sys.stdin.readline

n = int(input())
count = 0
six_n = 666

while True:
    if '666' in str(six_n):
        count += 1
    
    if count == n:
        print(six_n)
        break

    six_n += 1