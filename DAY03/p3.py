"""for DSA"""

# num = [1,2,3,4,5,6,7,7]

# uni = list(set(num))

# print("Original List: ", num)
# print("List Without Duplicates: ",uni)


# arr = [1,2,3,4,5]
# s = set(arr)

# x = 2
# if x in s:
#   print("found")
# else:
#   print("Not found")

# arr = [1, 2, 4, 5,7,8]
# n = 5

# full = set(range(1, n+1))
# missing = full - set(arr)
# print(missing.pop())

# arr = [1,2,3,4,5,2]

# seen = set()
# for num in arr:
#   if num in seen:
#     print("Duplicate",num)
#     break
#   seen.add(num)

# s = "Nikhil"
# print(len(set(s)))

l1 = [1,2,3]
l2 = [4,5,3]

if set(l1) & set(l2):
  print("List have common element")
else:
  print("No common element")

text = "Engineering"

uni = set(text)

print(uni)
print(len(uni))