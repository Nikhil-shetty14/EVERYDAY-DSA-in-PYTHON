# nums =[10,20,30,40,50,10]

# total = sum(nums)

# print("The total is:", total)

# print("largest:",max(nums))  
# print("Smallest:",min(nums))  

# nums.reverse()
# print("Reversed list:", nums)

# unique = list(set(nums))
# print(unique)


# nums = [8,9,1,2,3,4,5,6,7]

# # even = 0
# # odd = 0

# # for n in nums:
# #   if n % 2 == 0:
# #     even+=1
# #   else:
# #     odd+=1

# # print("Even",even)
# # print("odd",odd)
# nums.sort()
# print("second Largest: ",nums)

#merge

# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6]

# merged = a + b + c
# print (merged)

"""palindrome """

nums = [1,2,3,2,1,5]

if nums == nums[::-1]:
  print("Palindrome")
else:
  print("Not a palindrome")


"""Frequency"""

# nums = [1,2,3,4,4,4,4,4]

# freq = {}

# for n in nums:
#   freq[n] = freq.get(n,0) + 1

# print (freq) 


"""sort list without sort()"""
nums = [1,2,5,7,6,3]

for i in range(len(nums)):
  for j in range(i+1,len(nums)):
    if nums[i]> nums[j]:
      nums[i],nums[j] = nums[j],nums[i]

print(nums)