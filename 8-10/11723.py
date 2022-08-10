import sys
input = sys.stdin.readline

n = int(input())
arr = set()

for _ in range(n):
    command = sys.stdin.readline().strip().split()

    if len(command) == 1:
        if command[0] == "all":
            arr = set([i for i in range(1, 21)])
        else:
            arr = set()
    else:
        num = int(command[1])
        if command[0] == "add":
            arr.add(num)
        elif command[0] == "remove":
            arr.discard(num)
        elif command[0] == "check":
            if num in arr:
                print(1)
            else:
                print(0)
        elif command[0] == "toggle":
            if num in arr:
                arr.discard(num)
            else:
                arr.add(num)
