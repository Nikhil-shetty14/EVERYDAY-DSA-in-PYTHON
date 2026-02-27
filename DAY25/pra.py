"""Basic string Traversal"""

# def count_alphabet(s):
#   count = 0

#   for ch in s:
#     if ch.isalpha():
#       count += 1

#   return count

# print(count_alphabet("NIKHIL123"))

'''➤ Find First Non-Repeating Character'''

def first_non_repeating(s):
  freq = {}

  for ch in s:
    freq[ch] = freq.get(ch,0) + 1

  for ch in s:
    if freq[ch] == 1:
        return ch
      
  return None
   
print(first_non_repeating("aabccdd"))

"""Leet code Strings  3 Given a string s, find the 
length of the longest without duplicate characters."""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
       left = 0
       seen = {}
       max_length = 0 

       for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1

            seen[s[right]] = right

            current_length = right - left + 1

            max_length = max(max_length,current_length)
        return max_length
    