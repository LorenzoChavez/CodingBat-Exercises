# Given a string, return a new string made of every other char starting with the first.
# i.e "Hello" yields "Hlo"

def string_bits(str):
  new = ''
  for char in range(len(str)):
    if char % 2 == 0:
      new += str[char]    
  return new
