# Return the number of even ints in the given array.

def count_evens(nums):
  result = 0
  for i in nums:
    if i % 2 == 0:
      result += 1
  return result
