"""
1   2   3    4     5
0~1 2~7 8~19 20~37 38~61
1 6 12 18 24
"""
def f(number):
    n=1
    low=0
    up=1
    while True:
        if low < number <= up:
            return n
        low=up
        up+=6*n        
        n+=1

print(f(int(input())))