n=int(input())

cost=[25,10,5,1]
for _ in range(n):
    c=int(input())
    for i in range(4):
        temp=c//cost[i]
        c-=temp*cost[i]
        print(temp, end=' ')
    print()