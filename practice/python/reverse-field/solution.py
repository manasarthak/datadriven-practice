def reverse_str(s: str) -> str:
  n=len(s)
  temp=[0]*n
  idx=n-1
  for  ch in s:
    temp[idx]=ch
    idx-=1
  
  
  return ''.join(temp)
