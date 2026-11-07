def shortest_unique_metric_tag(metrics):
  n=len(metrics)
  ans=[""]*n
  early=set(range(n))#if all metrics get the req unique substring we should stop early
  #we start the outer loop for lowest substring length->longest
  max_len=max(len(metrics[i]) for i in range(n))
  for i in range(1,max_len+1):
    if not early:
      break
    temp={}
    for j in range(n):
      for k in range(len(metrics[j])-i+1):
        sub=metrics[j][k:k+i]
        temp[sub]=-1 if sub in temp else j
    #the other caveat here is we not only need the shortest unique from temp
    #we need the one which is the lexicographically smallest piece
    best={}
    for sub,who in temp.items():
      if who in early and (who not in best or sub<best[who]):
        best[who]=sub
    for idx,sub in best.items():
      ans[idx]=sub
      early.discard(idx)

  return ans
