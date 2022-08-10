import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, board):
    queue = deque()
    queue.append((x, y))
    board[x][y] = 2
    result = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= 0 or nx > n or ny <= 0 or ny > m:
                continue
            if board[nx][ny] != 1:
                continue

            queue.append((nx, ny))
            board[nx][ny] = 2
            result += 1
    return result


n, m, k = map(int, input().split())
board = [[0]*(m+1) for _ in range(n+1)]
answer = 0

for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        if board[i][j] == 1:
            answer = max(bfs(i, j, board), answer)

print(answer)
