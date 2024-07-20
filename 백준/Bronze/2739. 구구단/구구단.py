N = int(input())

for i in range(1,10): # range는 0부터 시작하므로 1로 따로 지정해줘야 함. 뒷 숫자-1까지 출력함.
    re = N*i
    print(str(N)+' * '+str(i)+' = '+str(re)) # 모든 변수들이 int이므로 str로 변형해야 출력 가능.

"""
숏코딩

a=b=int(input());exec("print(a,'*',b//a,'=',b);b+=a;"*9)
"""
