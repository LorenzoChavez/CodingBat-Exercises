# Given two strings, return True if either of the strings appears at the very end of the other string.
# Ignore upper/lower case differences (in other words, the computation should not be "case sensitive"). 

def end_other(a, b):
  a_in_b = a.lower() in b.lower()[-len(a):]
  b_in_a = b.lower() in a.lower()[-len(b):]
  return a_in_b or b_in_a
