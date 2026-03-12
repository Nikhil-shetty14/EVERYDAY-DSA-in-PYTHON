"""Reverse String """

# def reverse(s):
#     char = list(s)

#     left = 0

#     right = len(s) - 1

#     while left < right:
#         char[left],char[right] = char[right],char[left]

#         left +=1
#         right -=1

#     return "".join(char)
# print(reverse("Hello"))
# print(reverse("Nikhil"))
# print(reverse("SHEtty"))
        

"""Palindrome String"""

# def palindrome(s):
#     left , right = 0,len(s) - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
# print(palindrome("racecar"))

"""Frequency of Characters"""
def frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(frequency("Nikhil Shetty"))
