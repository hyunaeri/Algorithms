# 백준 10808 알파벳 갯수
import sys
read = sys.stdin.readline

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
S = read().rstrip()

for alpha in alphabet:
    print(S.count(alpha), end = ' ')