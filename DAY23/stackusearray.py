class Stack:
  def __init__(self):
    self.arr = []

  def push(self,x):
    self.arr.append(x)
  
  def pop(self):
    if not self.is_empty():
      return self.arr.pop()
    return "stack underflow"
  
  def peek(self):
    if not self.is_empty():
      return self.arr[-1]
    return "Stack is Empty"
  
  def is_empty(self):
    return len(self.arr) == 0

  def size(self):
    return len(self.arr)
  
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)


print(s.pop())   # 30
print(s.peek())  # 20
print(s.size())  #