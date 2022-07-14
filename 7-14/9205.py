import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((home_x, home_y))
    visited = [False] * n

    while queue:
        x, y = queue.popleft()
        if abs(x - goal_x) + abs(y - goal_y) <= 1000:
            return True

        for i in range(n):
            if visited[i] == False:
                nx, ny = p[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    visited[i] = True
                    queue.append([nx,ny])

    return False

T = int(input())
for _ in range(T):
    n = int(input())
    home_x, home_y = map(int, sys.stdin.readline().split())
    p = []
    for _ in range(n):
        p.append(list(map(int, sys.stdin.readline().split())))
    goal_x, goal_y = map(int, sys.stdin.readline().split())

    res = bfs()
    if res:
        print("happy")
    else:
        print("sad")
