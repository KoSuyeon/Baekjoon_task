T=int(input())

for _ in range(T):
  stk = []
  isVPS = True
  for ch in input():
    if ch == '(':
      stk.append(ch)
    else:
      if len(stk) > 0:
        stk.pop()
      else:
        isVPS = False
        break
  
  if stk:
    isVPS = False
  
  if isVPS:
    print("YES")
  else:
    print("NO")