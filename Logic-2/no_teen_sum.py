# Given 3 int values, a b c, return their sum.
# However, if any of the values is a teen -- in the range 13..19 inclusive -- then that # value counts as 0, except 15 and 16 do not count as a teens.
# Write a separate helper "def fix_teen(n):"that takes in an int value and returns that # value fixed for the teen rule.

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
  if n in range(13,15) or n in range(17,20):
    return 0
  else:
    return n
