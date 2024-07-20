n=int(input())                    # 과목수
li=list(map(int,input().split())) # 점수 리스트

m=max(li)       # 최댓값
s=sum(li)/m*100 # 점수 조작

print(s/n) # 평균

"""
숏코딩

n,*l=map(int,open(0).read().split())
print(sum(l)*100/max(l)/n)
# open(0).read(): 입력 전체를 하나의 문자열로 읽음.
# n, *l = ... : 첫번째 값을 n에 할당, 나머지 값을 l에 리스트로 할당
"""
