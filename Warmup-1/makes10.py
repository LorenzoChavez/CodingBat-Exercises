# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
  
  result = 0
  
  if a == 10 or b == 10 or a+b == 10:
    result = True
  else:
    result = False
    
  return result

