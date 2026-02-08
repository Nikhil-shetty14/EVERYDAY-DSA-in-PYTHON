"""Traversing"""
"""by for loop"""
# arr = [10,20,30,40]

# for num in arr:
#   print(num)


"""by indexing"""
# arr = [10,20,30,40]

# for i in range (len(arr)):
#   print(arr[i])


"""while loop"""
# arr = [10,20,30,40]

# i = 0
# while i < len(arr):
  
#   print((arr[i]))
#   i += 1

"""find sum """

# arr = [1,2,3,4]
# total = 0
# for num in arr:
#   total += num

# print("Sum =",total)

"""fIND max & min"""

# arr = [4,6,3,9,2]

# maxi = arr[0]
# mini = arr[0]

# for num in arr:
#   if num > maxi:
#     maxi = num
#   if num < mini:
#     mini = num

# print("Max = ", maxi)
# print("Min = ", mini)

"""Linear Search"""
# arr = list(map(int, input("Enter the numbers (space separated): ").split()))
# key = int(input("Enter key  : "))
# def linear_search(arr,key):
#   for i in range(len(arr)):
#     if arr[i] == key:
#       return i
#   return -1
# res = (linear_search([arr],key))

# if res != -1:
#   print("Element found at index:", res)
# else:  print("Element not found in the array.") 

"""Reverrse an array"""

def reverse(arr):
  l,r = 0, len(arr)-1

  while l < r:
    arr[l],arr[r] = arr[r],arr[l]
    l += 1
    r -= 1
  return arr
print(reverse([1,3,2,4]))