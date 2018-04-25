# Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  nines = 0
  for i in nums:
    if i == 9:
      nines+= 1
  return nines
