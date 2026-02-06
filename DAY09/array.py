"""two summ"""

# def two_sum(nums,target):
#   d = {}
#   for i ,num in enumerate(nums):
#     if target - num in d:
#       return [d[target-num],i]
#     d[num] = i

#   if target - num not in d:
#     print("items not found")

# print(two_sum([2,7,11,34,15,9],22))

"""Kadane's Algorithm"""
# def max_subarray(arr):
#   curr = maxi = arr[0]
#   for i in range (1,len(arr)):
#     curr = max(arr[i],curr + arr[i])
#     maxi = max(maxi ,curr)
#   return maxi
# print(max_subarray([-2,1,3,4,1,2,1,-5,-4]))


"""Rotating an array"""
def rotate(arr,k):
  k %= len(arr)
  arr[:] = arr[-k:] + arr[:-k]

print(rotate([1,2,3,4,5],2))

"""moves 0's to end of array"""
def move_zeroes(arr):
    index = 0
    for num in arr:
        if num != 0:
            arr[index] = num
            index += 1

    for i in range(index, len(arr)):
        arr[i] = 0

    return arr

print(move_zeroes([0,1,0,3,12]))

'''Check if Array is Sorted'''
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4]))