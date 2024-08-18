n=int(input())
cards=set(map(int,input().split()))
m=int(input())
q=list(map(int, input().split()))

li=[]
for i in q:
    if i in cards:
        li.append(1)
    else:
        li.append(0)
        
print(' '.join(map(str, li)))