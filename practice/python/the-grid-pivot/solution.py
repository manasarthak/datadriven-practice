def transpose_matrix(matrix: list) -> list:
  if not matrix:
    return []
  row,col=len(matrix),len(matrix[0])
  ans=[[0 for _ in range(row)] for _ in range(col)]
  for i in range (row):
    for j in range(col):
      ans[j][i]=matrix[i][j]
  
  return ans
