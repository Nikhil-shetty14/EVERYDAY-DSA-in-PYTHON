"""Anagram (Ignore Case & Spaces)"""

# def is_anagram_clean(s1, s2):
#     # Convert to lowercase and remove spaces
#     s1 = s1.lower().replace(" ", "")
#     s2 = s2.lower().replace(" ", "")
    
#     # If lengths differ → not anagram
#     if len(s1) != len(s2):
#         return False
    
#     count = {}
    
#     # Count characters from first string
#     for ch in s1:
#         count[ch] = count.get(ch, 0) + 1
    
#     # Decrease count using second string
#     for ch in s2:
#         if ch not in count or count[ch] == 0:
#             return False
#         count[ch] -= 1
    
#     return True


# print(is_anagram_clean("Dormitory", "Dirty Room"))

'''Group Anagrams'''

def group_anagrams(words):
    groups = {}
    
    for word in words:
        # Sort word to create key
        key = "".join(sorted(word))
        
        # Add word to corresponding group
        if key not in groups:
            groups[key] = []
        
        groups[key].append(word)
    
    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))


"""Find All Anagram Indices"""
def find_anagram_indices(s, p):
    result = []
    
    if len(p) > len(s):
        return result
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter(s[:len(p)])
    
    # Check first window
    if window_count == p_count:
        result.append(0)
    
    # Slide window
    for i in range(len(p), len(s)):
        window_count[s[i]] += 1                  # Add new character
        window_count[s[i - len(p)]] -= 1         # Remove old character
        
        # Remove zero count entries
        if window_count[s[i - len(p)]] == 0:
            del window_count[s[i - len(p)]]
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result


print(find_anagram_indices("cbaebabacd", "abc"))
