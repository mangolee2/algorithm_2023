import sys

input = sys.stdin.readline

def dfs(v):
    visited[v]=1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited[i]==0 and graph[v][i]==1:
            dfs(i)

n,m,v=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(m):
    a,b=map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)