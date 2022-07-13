n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

arr = sorted(arr, key = lambda x : (x[1],x[0]))

count = 1
end = arr[0][1]

for i in range(1,len(arr)):
    if arr[i][0] >= end:
        count += 1
        end = arr[i][1]

print(count)
