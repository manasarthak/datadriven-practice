import heapq
def merge_k_sorted(lists: list) -> list:
  #approach 2: using heaps
  if not lists:
    return []
  heap=[]
  for arr in lists:
    for i in range(len(arr)):
      heapq.heappush(heap,arr[i])
  ans=[]
  while heap:
    ans.append(heapq.heappop(heap))
  return ans
  
      
        






  return
