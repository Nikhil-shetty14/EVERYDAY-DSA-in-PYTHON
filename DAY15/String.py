"""string"""

"""A string is a sequencec of char"""

# s = "nikhil"
# Index:  0 1 2 3 4 5
#         n i k h i l

'''Length'''

'''Accessing Characters'''
s[0]      # first character
s[-1]     # last character

"""Traversing"""
for ch in s:
    print(ch)

"""Substring / Slicing"""
s[1:4]    # ikh
s[:3]
s[2:]

"""Important Built-in Methods"""
s.lower()
s.upper()
s.strip()
s.replace()
s.split()
" ".join(list)
s.find()