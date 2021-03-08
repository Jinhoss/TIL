# import sys
# sys.stdin = open('input.txt')

# 인덱스를 인자로 받아 길이가 L인 단어 완성하는 함수
def sol(idx):
    stack = []
    stack.append([lst[idx]])
    while stack:
        word = stack.pop()
        # 길이가 L이라면
        if len(word) == L:
            # 모음이 한 개 이상이고, 자음이 두 개 이상인지 확인
            if len([w for w in word if w in ['a','e','i','o','u']])>=1 and len([w for w in word if w not in ['a','e','i','o','u']])>=2:
                result.append(''.join(word))
        # 길이가 L이 아니라면 남은 리스트 중에 이전 글자보다 큰 글자 중에서 골라 담음
        for x in lst[idx+1:]:
            if x>word[-1] and len(word)<L:
                stack.append(word+[x])
# input 입력
L, C = map(int, input().split())
lst = list(input().split())
# 입력 받은 문자열 정렬
lst.sort()
result = []
# C-L보다 작은 index만 확인, 그 이상은 L을 만족할 수가 없음
for i in range(C-L+1):
    sol(i)
for w in sorted(result):
    print(w)

