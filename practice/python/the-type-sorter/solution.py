def filter_integers(items: list) -> list[int]:
  ans=[]
  for item in items:
    if isinstance(item,int) and not isinstance(item,bool):
      ans.append(item)
  return ans
