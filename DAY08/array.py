# """Array
# An array stores multipl valuues in a single variables
# """

# # arr = [10, 20, 30, 40]

# # print(arr[0])
# # arr.append(7)

# # print(arr)
# # """
# arr = [5, 2, 9, 1]

# print(arr[0])      # Access → 5
# arr.append(7)      # Insert end
# arr.insert(1, 8)   # Insert at index
# arr.remove(9)      # Remove value
# arr.pop()          # Remove last
# print(len(arr))    # Length
# """

# """"""

# """Traversing an Array  """

# # ar = [10, 20, 30, 40]

# # for num in ar:
# #   print(num)

# # for i in range(len(ar)):
# #    print(arr[i])
# """Linear search o(n)"""
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

"""Binary search o(log n)"""

def binary(arr,key):
    left,right = 0,len(arr) - 1
    while left <= right:
        mid = (left + right) //2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid+1
        else:
            right = mid - 1
    return -1

"""Reverse an array"""
arr = [10,20,30,40]
# arr.reverse()
# print(arr)

def reverse(arr):
    l , r = 0,len(arr)-1
    while l < r:
        arr[l],arr[r]  = arr[r],arr[l]
        l += 1
        r -= 1
reverse(arr)
print(arr)