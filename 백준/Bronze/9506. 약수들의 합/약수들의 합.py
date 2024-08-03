def out(n):
    li=[]
    for i in range(1,n):
        if n%i==0:
            li.append(i)
    if sum(li)==n:
        return f'{n} = '+' + '.join(map(str,li))
    else :
        return f"{n} is NOT perfect."
    
while True:
    n = int(input())
    if n == -1:
        break
    print(out(n))