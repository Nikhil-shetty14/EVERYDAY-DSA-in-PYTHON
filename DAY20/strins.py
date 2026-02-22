"""Find Common Characters Between Two Strings"""

# def common_characters(s1, s2):
#   result =""

#   for ch in set(s1):
#     if ch in s2:
#       result += ch
#   return result
# print(common_characters("Hello" , "world")) 

"""Toggle Case in a String"""
def toggle(s):
  result = ""

  for ch in s:
    if 'a' <= ch <= 'z':
      result += chr(ord(ch) - 32)
    elif 'A' <= ch <= 'Z':
      result += chr(ord(ch) + 32)
    else:
      result += ch

  return result
print(toggle("niKHiL")) 
