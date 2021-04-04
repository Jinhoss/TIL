import re
import sys
sys.stdin = open('input.txt')
n = int(input())
for _ in range(n):
    word = input()
    p = re.match('[A-F]?A+F+C+[A-F]?', word)
    if p and p.group() == word:
        print('Infected!')
    else:
        print('Good')
