# class Solution(object):
#     def romanToInt(self, s):
#         roman = {
#             'I':1,
#             'V':5,
#             'X':10,
#             'L':50,
#             'C':100,
#             'D':500,
#             'M':1000,
#         }

#         total = 0

#         for i  in range (len(s)):
#             if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
#                 total -= roman[s[i]]
#             else:
#                 total += roman[s[i]]

#         return total

"""Check if Two Strings are Isomorphic"""
# def is_isomorphic(s1, s2):
#     if len(s1) != len(s2):
#         return False
    
#     map1 = {}
#     map2 = {}
    
#     for i in range(len(s1)):
#         c1, c2 = s1[i], s2[i]
        
#         if c1 in map1 and map1[c1] != c2:
#             return False
        
#         if c2 in map2 and map2[c2] != c1:
#             return False
        
#         map1[c1] = c2
#         map2[c2] = c1
    
#     return True

# print(is_isomorphic("egg", "abd"))

"""Check if String Contains Only Digits"""
def is_all_digi(s):
  for ch in s:
    if ch < '0' or ch > '9':
      return False
  return True
print(is_all_digi("12345"))