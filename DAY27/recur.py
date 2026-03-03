"""Sum of N Natural numbers"""

# def sum (n):
#   if n == 0:
#     return 0
#   return n + sum(n-1)


# print(sum(5))

"""Fibonacci"""

# def fibo(n):
#   if n <= 1:
#     return n
#   return fibo(n-1) + fibo(n-2)

# print(fibo(10))

"""Reverse a string"""

# def reverse_string(s):
#   if len(s) == 0:
#     return s
#   return reverse_string(s[1:]) + s[0]
  
# print(reverse_string("Nikhil"))

"""Print All Subsets"""

# from sympy import subsets


# def subset(s,current="",index=0):
#   if index == len(s):
#     print(current)
#     return
  
#   #include
#   subset(s,current + s[index],index + 1)

#   #exclude
#   subset(s,current,index + 1)

# subsets("abc")


"""GEnerate all permutations"""

def permutation(s,current=""):
  if len(s) == 0:
    print(current)
    return
  
  for i in range(len(s)):
    remaining = s[:i] + s[i+1:]

    permutation(remaining,current + s[i])

permutation("abc") 