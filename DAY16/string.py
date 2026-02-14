"""Reverse a string. """

# def reverse(s):
#   s = list(s)

#   left = 0
#   right = len(s) - 1

#   while left  < right :
#     s[left],s[right] = s[right],s[left] 

#     left += 1
#     right -= 1

#     return "".join(s)
  
# print(reverse("Nikhil"))
# print(reverse("123456"))


"""palindrome check"""

# def is_palindrome(s):
#   left = 0
#   right = len(s) - 1

#   while left < right:
#     if s[left] != s[right]:
#       return False
    
#     left += 1
#     right -= 1

#   return True
# print(is_palindrome("nikhil"))

"""Check Anagram"""

# def is_anagram(s1,s2):
#   if len(s1) != len(s2):
#     return False
  
#   count = {}

#   for ch in s1:
#     count[ch] = count.get(ch,0) + 1


#   for ch in s2:
#     if ch not in count or count[ch] == 0:
#       return False
#     count[ch] -= 1

#   return True

# print(is_anagram("ass","ass"))

"""Char Frequency Counter"""

# def char_freq(s):
#   freq = {}

#   for ch in s:

#     freq[ch] = freq.get(ch,0) + 1

#   return freq


# print(char_freq("Nikhil Shetty"))

"""Remove Duplicate"""

# def remove_dupli(s):
#   seen = set()
#   res  = []

#   for ch in s:
#     if ch not in seen:
#       seen.add(ch)
#       res.append(ch)

#   return "".join(res)
# print(remove_dupli("programming"))

"""First Non repeating char"""

def first(s):
  freq = {}

  for ch in s:
    freq[ch] = freq.get(ch,0) + 1

  for ch in s:
    if freq[ch] == 1:
      return ch
  return None
print(first("aaddjdd"))