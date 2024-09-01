n=int(input())
""" 메모리초과
a=[1 for i in range(n)]

for j in range(2,n+1):
    for i in range(j-1,n,j):
        a[i]=1-a[i]
        
print(sum(a))
"""
# 1부터 n까지의 완전 제곱수를 계산
c = 0
i = 1
while i*i <= n:
    c += 1
    i += 1

print(c)
