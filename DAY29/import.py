# import wikipedia

# print(wikipedia.summary("Rajeev Institute of technology"))

"""Binary Search Implementation"""

def binary(arr,left,right,target):

  if left > right:
    return -1
  
  mid = (left+right) // 2

  if arr[mid] == target:
    return mid
  
  elif arr[mid] > target:
    return binary(arr,left,mid-1,target)
  
  else:
    return binary(arr,mid+1,right,target)
  
arr = [1,3,5,7,9]

print(binary(arr,0,len(arr)-1,7))

"""Check if Array is sorteced"""

def is_sorted(arr,n):
  if n == 1:
    return True
  
  if arr[n-1] < arr[n-2]:
    return False
  
  return is_sorted(arr,n-1)
arr = [1,2,6,4,5]
print(is_sorted(arr,len(arr)))


"""Climbing stairs"""

def climb(n):
  if n == 0 or n == 1:
    return 1
  return climb(n-1) + climb(n-2)

print(climb(5))