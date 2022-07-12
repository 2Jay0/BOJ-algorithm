import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int,input().split()))

heapq.heapify(arr)

while True:
    if m == 0:
        print(sum(arr))
        break
    fir = heapq.heappop(arr)
    sec = heapq.heappop(arr)
    heapq.heappush(arr, fir + sec)
    heapq.heappush(arr, fir + sec)
    m -= 1
