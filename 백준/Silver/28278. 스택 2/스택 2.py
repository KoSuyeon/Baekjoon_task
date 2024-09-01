# Stack:LIFO
# 1: stack.append(정수 X)
# 2: print(stack.pop()) else: print(-1)
# 3: print(len(stack))
# 4: print(1 if len(stack)==0) else print(0)
# 5: print(stack[-1]) else: print(-1)
import sys

n=int(input())

stack = []

for _ in range(n):
    r = sys.stdin.readline().split()

    if r[0] == '1':
        stack.append(r[1])

    elif r[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif r[0] == '3':
        print(len(stack))

    elif r[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif r[0] == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])