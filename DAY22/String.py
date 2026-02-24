# """Valid String"""

# def is_valid_palin(s):
#   l,r=0,len(s)-1

#   while l < r:

#     while l < r and not s[l].isalnum():
#       l += 1

#     while l < r and not s[r].isalnum():
#       r -=1

#     if s[l].lower() != s[r].lower():
#       return False
    
#     l +=1
#     r -= 1

#   return True

# print(is_valid_palin( "A man ,a plan,a canal:panama"))


"""Check if string Contain only Unique Char"""

def has_unique_characters(s):
    seen = set()
    
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    
    return True


print(has_unique_characters("abcde"))