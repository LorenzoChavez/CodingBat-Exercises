# Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string 

def missing_char(str, n):
  
  new_string=''

  if n in range(0,len(str)):
   new_string = str[:n] + str[n + 1:]

  return new_string
