def mst_prim(n,G):
    key=[float('inf') for _ in range(n)]
    pi=[None for _ in range(n)]
    visited=[False for _ in range(n)]
    key[0]=0
    for _ in range(n):
        min_key=float('inf')
        start=-1
        for i in range(n):
            if key[i]<min_key and not visited[i]:
                min_key=key[i]
                start=i
        visited[start]=True
        for next_v,next_w in G[start]:
            if next_w<key[next_v] and not visited[next_v]:
                key[next_v]=next_w
                pi[next_v]=start
    return sum(key)

def solution(n, costs):
    sol_graph={}
    for x in costs:
        if x[0] not in sol_graph:
            sol_graph[x[0]]=set()
        if x[1] not in sol_graph:
            sol_graph[x[1]]=set()
        sol_graph[x[0]].add((x[1],x[2]))
        sol_graph[x[1]].add((x[0],x[2]))
    return mst_prim(n,sol_graph)