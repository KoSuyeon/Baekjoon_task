x_c=[]
y_c=[]

for _ in range(3): #무조건 3점을 받으니까
    x,y = map(int,input().split())
    x_c.append(x) #30 10 10
    y_c.append(y) #20 10 20

def miss_point(one):
    for o in one:
        if one.count(o)==1 :
            return o
        
print(miss_point(x_c),miss_point(y_c)) 