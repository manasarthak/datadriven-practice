def manual_sort(nums):
  #use this to revise all types of sorting techniques.
  #1. Selection sort (#shift elements right until the slot is found)
  #                  (other way to think is afgter i iterations elements seen till 0-i are sorted in place and rest remain unseen)
  for i in range(len(nums)):
    temp,j=nums[i],i-1
    while j>=0 and nums[j]>temp:
      nums[j+1]=nums[j]
      j-=1
    nums[j+1]=temp
  return nums
