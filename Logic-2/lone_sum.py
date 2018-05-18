# Given 3 int values, a b c, return their sum. 
# However, if one of the values is the same as another of the values, it does not count towards the sum.

def lone_sum(a, b, c):
  new_sum = [a, b, c]
  if a == b:
    if b == c:
      new_sum.remove(a)
      new_sum.remove(b)
      new_sum.remove(c)
    else:
      new_sum.remove(a)
      new_sum.remove(b)
  elif a == c:
    new_sum.remove(a)
    new_sum.remove(c)
  elif b == c:
    new_sum.remove(b)
    new_sum.remove(c)
  return sum(new_sum)
