# Daily_Algorithm





## 📅 매일 한 문제 이상 풀기

문제를 풀고 시간적 여유가 있을때 velog에 문제풀이 게시

 [알고리즘 문제풀이](https://velog.io/@jinho0705)



<br/>





## :pencil: 자주 까먹거나, 아직 낯선 개념 기록

<br/>

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

<br/>

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



<br/>

#### 파이썬 표준출력 채움문자와 숫자 표시형식  

```
{[인덱스]:[채움문자][정렬][길이][,|_][형식문자]
공백을 채움문자로 채워줍니다.
, : 천단위 마다 콤마를 붙여줍니다.
_ : 천단위 마다 밑줄을 붙여줍니다.
e : 숫자를 지수 형식으로 만들어 줍니다.
= : 숫자 형식에만 사용합니다. 부호를 항상 제일 앞에 출력합니다.
```

<br/>

#### 크루스칼 알고리즘(O(ElogE))

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
rersult = 0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i
    
# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용 순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))
    
# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며 사이클이 발생하지 않는 경우, 집합에 포함
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
```

<br/>

#### 위상 정렬 알고리즘(O(V + E))

- 위상 정렬은 DAG에 대해서만 수행 가능
- 여러 가지 답이 존재할 수 있다.
- 모든 원소를 방문하기 전에 큐가 빈다 => 사이클이 존재
- 스택을 활용한 DFS로도 위상 정렬 수행 가능



```python
from collections import deque

# 노드의 개수와 간선의 개수를 입력
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # a에서 b로 이동 가능
    # 진입 차수 1 증가
    indegree[b] += 1
    
# 위상 정렬 함수

def topology_sort():
    result = [] # 결과 리스트
    q = deque() # 큐 생성
    
    # 처음 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 꺼낸 원소와 연결된 노드들의 진입차수를 1씩 감소
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
        # 위상 정렬을 수행한 결과 출력
       	for i in result:
            print(i, end = ' ')
topology_sort()
                
```

<br/>



#### 세그먼트 트리(O(logN))

세그먼트 트리의 리프 노드와 리프 노드가 아닌 다른 노드는 다음과 같은 의미를 가진다.

- 리프 노드: 배열의 그 수 자체
- 다른 노드: 왼쪽 자식과 오른쪽 자식의 합을 저장

```python
import sys
input = sys.stdin.readline

# 세그먼트 트리 생성
def init(node, start, end):
    mid = (start + end) // 2
    # node가 leaf 노드인 경우 배열의 원소 값을 반환
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        # 재귀함수를 이용하여 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장
        tree[node] = init(node * 2, start, mid) + init(node * 2, mid + 1, end)
        return tree[node]

# 구간 합 구하기
# node가 담당하는 구간 [start, end]
# 합을 구해야하는 구간 [left, right]
def subSum(node, start, end, left, right):
    mid = (start + end) // 2
    # 겹치지 않기 대문에, 더 이상 탐색을 이어갈 필요가 없는 경우
    if left > end or right < start:
        return 0 
    # 구해야하는 합의 범위는 [left, right]인데, [start, end]는 그 범위에 모두 포함됨
    # 그 node의 자식도 모두 포함되기 때문에 더 이상 호출하지 않음
    if left <= start and end <= right:
        return tree[node]
    
    # 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작해야한다.
    return subSum(node * 2, start, mid, left, right) + subSum(node * 2 + 1, mid + 1, end, left, right)

def update(node, start, end, index, diff):
    mid = (start + end) // 2
    
    if index < start or index > end:
        return
    
    tree[node] += diff
    
    # 리프 노드가 아닌 경우에는 자식도 변경해줘야 하기 때문에 검사해야함.
    if start != end:
        update(node * 2, start, mid, index, diff)
        update(node * 2, mid + 1, end, index, diff)
        
n, m , k = map(int, input().rstrip().split())

l = []
tree = [0] * 3000000

for _ in range(n):
    l.append(int(input().rstrip()))
    
init(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().rstrip().split())
    
    if a == 1:
        b -= 1 
        diff = c - l[b]
        l[b] = c
        update(1, 0, n - 1, b, diff)
    elif a == 2:
        print(subSum(1, 0, n - 1, b - 1, c - 1))
        
```

<br/>



#### 정규표현식 그룹 나누기



```python
>>> p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
>>> print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
# 010-1234-1234 park
# sub의 바꿀 문자열에 \g<그룹이름> 을 사용하면 정규식의 그룹 이름을 참조
# (?P<name>표현식) => 그룹으로 지정한 표현식에 이름을 지정 (default = index)
```

