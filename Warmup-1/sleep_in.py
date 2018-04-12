# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
  
  result = 0
  
  if weekday == True and vacation == False:
    result = False
  else:
    result = True
  
  return result
