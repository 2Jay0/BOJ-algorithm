import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if check[n] == 0:
                check[n] = check[node] + 1
                queue.append(n)

n = int(input())
x, y = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
check = [0] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(x)
print(check[y] if check[y] > 0 else -1)
