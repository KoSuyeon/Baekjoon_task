n=int(input())
li=list(map(int,input().split()))

m=max(li)
s=sum(li)/m*100

print(s/n)