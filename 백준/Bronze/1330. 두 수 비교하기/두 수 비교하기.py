# input()는 str로 처리되므로 map()을 통해 int로 type을 바꿔줘야 함.
A,B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

"""
숏코딩

a,b=map(int,input().split())
print(['><'[a<b],'=='][a==b])
# ><'[a < b]: a < b의 결과에 따라 '>' 또는 '<'를 반환
# a < b가 True이면 인덱스 1이 선택되어 '>'가 반환되고, False이면 인덱스 0이 선택되어 '<'가 반환
# '=='][a == b]: [a == b]는 a == b가 True일 경우 인덱스 1을 선택하여 '=='을 반환하고, False일 경우 인덱스 0을 선택하여 앞서 결정된 '>' 또는 '<'을 반환
"""
