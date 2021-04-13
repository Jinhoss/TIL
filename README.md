# Daily_Algorithm





## 📅 매일 한 문제 이상 풀기

문제를 풀고 시간적 여유가 있을때 velog에 문제풀이 게시

 [알고리즘 문제풀이](https://velog.io/@jinho0705)



<br/>





## :pencil: 자주 까먹거나, 아직 낯선 개념 기록



#### 다익스트라 알고리즘: 우선순위 큐(O(ElogV))

```python
# 우선순위큐 x, 다익스트라 알고리즘 => O(V**2)
import heapq
import sys
input = sys.stdin.readline
INF = float('inf')

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b로 가는 비용이 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 최단 거리인 노드에 대한 정보를 꺼낸다
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 노드라면 무시한다.
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
        
    
    
```



#### 서로소 집합 자료구조: 경로 압축

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def unidon_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 부모 노드가 더 작은 숫자 쪽으로 합침
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i
# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end = '')
for i in range(1, v + 1):
    print(find_parent(parent, i), end = ' ')
    
print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end = '')
for i in range(1, v + 1):
    print(parent[i], end = ' ')
```





#### 파이썬 표준출력 채움문자와 숫자 표시형식

```
{[인덱스]:[채움문자][정렬][길이][,|_][형식문자]
공백을 채움문자로 채워줍니다.
, : 천단위 마다 콤마를 붙여줍니다.
_ : 천단위 마다 밑줄을 붙여줍니다.
e : 숫자를 지수 형식으로 만들어 줍니다.
= : 숫자 형식에만 사용합니다. 부호를 항상 제일 앞에 출력합니다.
```

