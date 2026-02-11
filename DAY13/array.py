"""Largest element"""

# def largest(arr):
#   maxi = arr[0]
#   for num in arr:
#     if num > maxi:
#       maxi = num
#   return maxi

# print(largest(arr))

"""Second largest element"""
# arr = [10,20,34,57,78,79]
# def second_largest(arr):
#   first = second = float ('-inf')

#   for num in arr:
#     if num > first:
#       second = first 
#       first = num 
#     elif num > second and num != first:
#       second = num 

#   return second 

# print(second_largest(arr))

"""Check if ARRAY is sorted"""

# arr = [2,4,6,8,4,9]
# def is_sorted(arr):
#   for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#       return False
#     return True
 
  
# print("yes")

"""reverse"""

# arr = [1,2,3,4]
# # def reverse(arr):
# #   l,r = 0,len(arr)-1
# #   while l < r:
# #     arr[l],arr[r] = arr[r],arr[l]
# #     l += 1
# #     r -=1
# #   return arr
# # print(reverse(arr))

# print(arr[::-1])


"""Dutch Flag"""

arr = [0,1,2,0,1,2,0,1]
def sort012(arr):
  low = mid =0
  high = len(arr) - 1

  while mid <= high:
    if arr[mid] == 0:
      arr[low],arr[mid] = arr[mid],arr[low]
      low += 1
      mid += 1
    elif arr[mid] == 1:
      mid += 1
    else:
      arr[mid] , arr[high] = arr[high] , arr[mid]
      high -= 1

  return arr

print(sort012(arr))