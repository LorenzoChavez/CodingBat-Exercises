# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

def has22(nums):
  str_nums = ''.join(str(i) for i in nums)
  return '22' in str_nums
