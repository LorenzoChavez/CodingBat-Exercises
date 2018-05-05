# Given 2 ints, a and b, return their sum. 
# However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

def sorta_sum(a, b):
  sums = a + b
  forbidden = 10 <= sums < 20
  if forbidden:
    return 20
  else:
    return sums
