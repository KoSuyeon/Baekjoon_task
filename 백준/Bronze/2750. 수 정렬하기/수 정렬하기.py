N = int(input())
numbers = []

for _ in range(N):
    number = int(input())
    numbers.append(number)

numbers.sort() # 오름차순으로 정렬

for num in numbers: #한 줄씩 출력
    print(num)
    
"""
N = int(input())
numbers = sorted([int(input()) for _ in range(N)])
for num in numbers:
    print(num)
"""
