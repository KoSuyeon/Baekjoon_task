n=int(input())
li=list(map(int,input().split()))

for i in li:
    if i <2:
        n-=1
    else:
        for j in range(2,i): #2부터 i-1까지
            if i % j == 0:   #i를 j로 나누면서 나눠떨어지면 i가 소수 아님.
                n-=1
                break
print(n)
    
