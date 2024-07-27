n=[list(map(int,input().split())) for _ in range(9)]
m=max(map(max,n))

for i in range(9):
    for j in range(9):
        if n[i][j] == m:
            max_pos=(i+1,j+1)
            break

print(m)     
print(max_pos[0],max_pos[1])

"""
n=open(0).read().split()
print(n[i:=n.index(max(n,key=int))],i//9+1,i%9+1)
#i//9+1, i%9+1 : 0 기반 인덱스를 1 기반으로 변환하기 위함
"""
