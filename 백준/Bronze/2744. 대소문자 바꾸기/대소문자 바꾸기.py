import sys
read = sys.stdin.readline

str = read().rstrip()
result = ""

for s in str:
    if s.islower():
        result += s.upper()
    else:
        result += s.lower()

print(result)