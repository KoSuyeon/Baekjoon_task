a,b,c=map(int,input().split())
#가장 큰 변이 다른 두 변의 합보다 크면 삼각형 못 만들어.
def rec(a,b,c):
    li=sorted([a,b,c])
    if li[0]+li[1] > li[2]:
        return sum(li)
    elif li[0]+li[1] <= li[2]:
        return 2*(li[0]+li[1])-1
    #(li[0]+li[1]+li[2])-(li[2]-li[0]-li[1]+1)
    #2(li[0]+li[1])-1

print(rec(a,b,c))