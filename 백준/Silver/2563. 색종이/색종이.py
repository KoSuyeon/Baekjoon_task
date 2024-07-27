n=int(input())
m=[[0]*100 for _ in range(100)]

for _ in range(n):
    a,b= map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            m[i][j]=1
            
area=sum(map(sum,m))
print(area)

"""
print(len({(int(s[:2])+i//10,int(s[2:])+i%10)for s in[*open(0)][1:]for i in range(100)}))
"""
