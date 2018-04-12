# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
  
  result = 0
  
  if a == b:
    result =  (a+b) * 2
  else:
    result = a+b
  
  return result
