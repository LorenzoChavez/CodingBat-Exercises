# Given a string, return a new string where "not " has been added to the front. 
# However, if the string already begins with "not", return the string unchange

def not_string(str):
  result = 0  
  if str[:3] == 'not':
    result = str
  else:
    result = 'not ' + str
    
  return result

