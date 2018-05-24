# We want make a package of goal kilos of chocolate.
# We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars.
# Return -1 if it can't be done.

def make_chocolate(small, big, goal):
  big_needed = goal // 5
  if big_needed >= big:
    small_needed = goal - (5*big)
  else:
    small_needed = goal - (5*big_needed)
  
  if small < small_needed:
    return -1
  else:
    return small_needed
