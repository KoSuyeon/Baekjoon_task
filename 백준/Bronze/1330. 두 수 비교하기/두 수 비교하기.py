# input()는 str로 처리되므로 map()을 통해 int로 type을 바꿔줘야 함.
A,B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
