# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
  
  new_str = ''
  
  if len(str) < 2:
    new_str = str
  else:
    new_str = str[-1] + str[1:-1] + str[0]
  return new_str

