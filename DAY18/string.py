"""Reverse Strting"""

# def reverse(s):
#   s = list(s)
#   left ,right = 0,len(s) - 1

#   while left < right:
#     s[left], s[right] = s[right] , s[left]

#     left +=1
#     right -=1

#   return "".join(s)

# print(reverse("nikhil"))

"""Check Palindrome"""

# def is_palin(s):
#   left,right = 0,len(s) -1

#   while left < right :
#     if s[left] != s[right]:
#       return False
#     left += 1
#     right -= 1

  
#   print(f"{s} is palindrome")
#   return ""

# print(is_palin("madam"))

"""Remove duplicate"""

# def remove(s):
#   seen = set()
#   res = []

#   for ch in s:
#     if ch not in seen:
#       seen.add(ch)
#       res.append(ch)

#   return"".join(res)

# print(remove("shetty"))
''

"""Check string Rotation"""

def is_rotation(s1,s2):
  if len(s1) != len(s2):
    return False
  return s2 in (s1+s1)

print(is_rotation("abcd","deabc"))