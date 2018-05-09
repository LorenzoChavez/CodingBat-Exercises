# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7.
# every 6 will be followed by at least one 7. Return 0 for no numbers.

def sum67(nums):
  new_nums = nums[:]
  if new_nums == []:
    return 0
  
  while 6 in new_nums:
    start_6 = new_nums.index(6)
    end_7 = new_nums.index(7,start_6)
    del(new_nums[start_6:end_7+1])
        
  return sum(new_nums)
