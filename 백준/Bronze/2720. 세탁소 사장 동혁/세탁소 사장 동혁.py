n=int(input())

cost=[25,10,5,1]
for _ in range(n):
    c=int(input())
    for i in range(4):
        temp=c//cost[i]
        c-=temp*cost[i]
        print(temp, end=' ')
    print()

"""
for i in[*open(0)][1:]:c=int(i);print(c//25,c%25//10,c%25//5%2,c%5)
"""
