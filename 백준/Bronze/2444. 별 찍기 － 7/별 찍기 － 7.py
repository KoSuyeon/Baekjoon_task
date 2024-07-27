n=int(input())

for i in range(n):
    print(' '*(n-i-1)+'*'*(2*i+1))
    
for i in range(n-2,-1,-1):
    print(' '*(n-i-1)+'*'*(2*i+1))

"""
n=m=int(input())
while l:=n-abs(m:=m-1):
   print(' '*(n-l)+'*'*(l*2-1))
"""
