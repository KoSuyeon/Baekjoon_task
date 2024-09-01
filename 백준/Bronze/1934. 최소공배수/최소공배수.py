n=int(input())

# 최대공약수 G : greatest common measure
# 최대공배수 L : least common multiple
# 자연수 A,B에 대하여, A*B=L*G
# L=G*(A를G로나눈몫)*(B를G로나눈몫)=A*B/G

# 𝑎를 𝑏로 나눈 나머지를 𝑟이라 할 때, 
# 𝑎와𝑏의 최대공약수는 𝑏와 𝑟의 최대공약수와 같다는 원리를 사용합니다. 
# 이를 반복하여 나머지가 0이 될 때의  𝑏값이 최대공약수가 됩니다.
def gcm(a, b):       #6,10
    while b>0:       # 10   6   4   2
        a,b = b, a%b #10,6 6,4 4,2 2,0
    return a         #2
"""
def lcm(a,b):
    return a*b / gcm(a,b) #6*10/2=30
"""
# 정수 나눗셈
def lcm(a,b):
    return a*b // gcm(a, b)

for _ in range(n):
    A,B=map(int, input().split())
    print(lcm(A,B))

