n=int(input())

for _ in range(n):
    r,s=input().rstrip().split()
    for i in s :
        #문자 i를 정수 r번 반복하여 출력합니다.
        #end=''는 줄바꿈을 하지 않고 다음 출력과 이어지게 합니다.
        print(i*int(r), end='') 
    print()



"""
for r,_,*s,_ in[*open(0)][1:]:print(''.join(c*int(r)for c in s))
#[*open(0)][1:]는 전체 입력을 리스트로 만들고 첫 번째 줄을 제외합니다. es.['3 ABC\n', '5 /HTP\n']
#r은 반복할 횟수, s는 반복할 문자열의 문자 리스트
#c*int(r)for c in s는 문자열 s의 각 문자 c를 정수 r번 반복하여 리스트로 만듭니다.
"""
