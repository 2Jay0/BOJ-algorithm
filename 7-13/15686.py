import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))
        if arr[i][j] == 2:
            chicken.append((i, j))


cnt = 1e+9
for i in range(1, m+1):
    for combi in list(combinations(range(len(chicken)), i)):
        entire = 0
        for h_idx in range(len(house)):
            real_dist = 1e+9
            for c in combi:
                dist = abs(house[h_idx][0] - chicken[c][0]) + abs(house[h_idx][1] - chicken[c][1])
                real_dist = min(dist, real_dist)
            entire += real_dist
        cnt = min(entire, cnt)

print(cnt)
