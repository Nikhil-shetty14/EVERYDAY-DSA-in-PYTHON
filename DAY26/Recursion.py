"""Recursion"""

def factorial(n):

  if n == 0 or n == 1:
    return 1
  
  else:
    return n * factorial(n - 1)
  
print(factorial(5)) # 120

"""Print Numbers 1 to N"""

def print_numbers(n):
  if n == 0:
    return
  
  print_numbers(n - 1)
  print(n)

print_numbers(5) # 1 2 3 4 5