import re
# import sys
# sys.stdin = open('input.txt')
while True:
    try:
        x = input()
        while True:
            word = re.sub('BUG', '', x)
            if word == x:
                break
            x = word
        print(x)
    except:
        break