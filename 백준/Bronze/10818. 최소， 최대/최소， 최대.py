n=int(input())

li=list(map(int,input().split()))
    
print(min(li), max(li))

"""
숏코딩

print(min(s:=[*map(int,[*open(0)][1].split())]),max(s))
# [*open(0)] : open(0)은 표준입력을 의미하며, 이를 리스트로 변환. *는 모든 줄을 읽는 다는 뜻.
# [*open(0)][1] : 두번째 줄을 가져옴.
# [*open(0)][1].split() : 두번째 줄을 공백단위로 나누오 리스트로 만듦.
# map(int, ...) : 문자열 리스트를 정수 리스트로 변환.
# :=는 월러스 연산자라 불리며, 표현식 안에서 변수를 할당할 수 있게 함. 즉, 정수 리스트를 변수 s에 저장
"""
