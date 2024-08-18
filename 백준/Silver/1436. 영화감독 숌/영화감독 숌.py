def find_666(n):
    count = 0
    number = 666  # 종말의 수 시리즈의 첫 번째 숫자는 666부터 시작
    while True:
        if '666' in str(number):  # 현재 숫자가 '666'을 포함하는지 확인
            count += 1
            if count == n:  # n번째 종말의 수를 찾았다면
                return number
        number += 1  # 다음 숫자로 이동

# 입력 받은 N 값에 따라 해당하는 종말의 수를 찾아 출력
N = int(input())
print(find_666(N))
