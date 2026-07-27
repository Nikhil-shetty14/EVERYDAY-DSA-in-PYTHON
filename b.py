def bubble (arr):
  n = len(arr)

  for i in range(n):
    swapped = False

    for j in range(0,n-i-1):
      if arr[j] > arr[j + 1]:
        arr[j] , arr[j + 1] = arr[j + 1], arr[j]
        swapped = True

    if not swapped:
      break

  return arr

arr = [54,67,25,12,33,90]

print("Original array:", arr)
sorted_arr = bubble(arr)
print("Sorted array:", sorted_arr)















