import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
ans = []
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline().strip()))

cnt = 0
while len(heap) != 1:
    fir = heapq.heappop((heap))
    sec = heapq.heappop((heap))

    cnt += fir + sec
    heapq.heappush(heap, fir + sec)

print(cnt)
