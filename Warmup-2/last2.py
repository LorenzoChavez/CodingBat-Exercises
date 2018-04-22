# Given a string, return the count of the number of times that a substring length 2 appears in the string
# Also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
  result = 0
  substring = str[-2:]
  
  if len(str) > 3:
    string = str[:(len(str)-2)]
    for letter in range(len(string)):
      if string[letter:(letter+2)] == substring:
        result+=1
      else:
        result+=0
  else:
    result = 0
  return result


