 #  Linear Search

def linear (arr,target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

arr = [5,3,8,2,9,2,7]
target = 9
result = linear(arr,target)
if result != -1:  print(f"Element {target} found at index {result}")
else: print(f"Element {target} not found")

