h,m = map(int,input().split())

m-=45 # 분이 45분 줄어듦.
if m<0:
    m+=60  # 이미 음수이므로 60분에 + 
    h-=1   # 시가 1시간 줄어듦
    if h<0:
        h=23 # 0시일 경우 23시가 되어야하므로
    
print(h,m)

"""
숏코딩

a,b=map(int,input().split())
print((a-(b<45))%24,(b-45)%60)

"""
