# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  nums_str = "".join(str(e) for e in nums)
  if "123" in nums_str:
    return True
  else:
    return False
