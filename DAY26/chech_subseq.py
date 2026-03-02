"""Check  subsequence"""

def is_subsequnce(s,t):

  i = 0

  for ch in t:
    if i < len(s) and s[i] == ch:
      i += 1

  return i == len(s)

print(is_subsequnce("abc","hbgdc"))

"""Valid Palindrome"""

def is_palin(s):
  l = 0
  r = len(s) - 1 

  while l < r:
    if s[l] != s[r]:
      return False
    
    l += 1
    r -= 1

  return True

print(is_palin("assaassa")) 