def merge_k_sorted(lists: list) -> list:
  #approach 1: divide and conquer
  def merge(a,b):
    if not b:
      return a
    merged=[]
    n1,n2=len(a),len(b)
    i,j=0,0
    while i<n1 and j<n2:
      if a[i]<=b[j]:
        merged.append(a[i])
        i+=1
      else:
        merged.append(b[j])
        j+=1
    while i<n1:
      merged.append(a[i])
      i+=1
    while j<n2:
      merged.append(b[j])
      j+=1
    return merged
  if not lists:
    return []
  while len(lists)>1:
    ans=[]
    for i in range(0,len(lists),2):
      ans.append(merge(lists[i],lists[i+1] if i+1<len(lists) else None))
    lists=ans
  return lists[0]
      
        






  return
