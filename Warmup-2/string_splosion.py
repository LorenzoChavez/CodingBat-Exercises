# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):

  result = ''

  for letter in range(len(str)):
    result = result + str[:letter+1]

  return result
