# Given a string, we'll say that the front is the first 3 chars of the string. 
# If the string length is less than 3, the front is whatever is there. 
# Return a new string which is 3 copies of the front.

def front3(str):
  new_string = ''
  
  if len(str) < 3:
    new_string = str * 3
  else:
    new_string = str[0:3] * 3
  return new_string
