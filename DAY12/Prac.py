"""Find sum of Array elements using for loop"""

# arr = [1,2,3,4,5]
# total = 0 
# for num in arr:
#   total += num

# print(total)

"""Linear"""

# arr  = [3,7,1,8]
# key = 7

# found = False
# for num in arr:
#   if num == key:
#     found = True

# print(found) 

'''Remove Duplicates'''

# arr = [1,2,3,4,2]
# unique = []

# for num in arr:
#   if num not in unique:
#     unique.append(num)
  
# print(unique)
# print("Removed element is ",num)

"""Rotate array"""

# def rotate(arr,k):
#   k %= len(arr)
#   return arr[-k:] + arr[:-k]

# print(rotate([1,2,3,4],2))

"""Count Even & odd"""
arr = [1,2,3,4,5]

even =0
odd = 0

for num in arr:
  if num % 2 == 0:
    even += 1
    print(even)
  else:
    odd  += 1
    print(odd)
  
print("Even : ",even)
print("Odd : ",odd)

