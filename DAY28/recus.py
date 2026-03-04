# """Tower of Hanoi"""

# def hanoi(n,source,helper,destination):
#   if n == 1:
#     print(f"Move disk 1 from {source} to {destination}")
#     return 
#   hanoi(n-1,source,destination,helper)
#   print(f"Move disk {n} from {source} to {destination}")
#   hanoi(n-1,helper,source,destination)

# hanoi(4,'A','B','C')

# """Print all subsets"""
# def subsets(s,current="",index=0):
#   if index == len(s):
#     print(current)
#     return
  
#   subsets(s,current + s[index],index + 1)

#   subsets(s,current,index + 1)

# subsets("Nikhil")

# """Power """

# def power(x,n):
#   if n== 0:
#     return 1
  
#   return x * power(x,n-1)

# print(power(2,3))

"""Stack Implementation"""

# stack = []

# #push
# stack.append(10)
# stack.append(20)
# stack.append(30)

# #pop

# print(stack.pop())

# print(stack)

"""Pop from stack using recursion"""

def pop_stack(stack):
  if len(stack) == 0:
    return "stack Underflow"

  top = stack[-1]
  stack.pop()
  return top
stack = [10,20,30,40]

print(pop_stack(stack))

print(stack)

