"""stack Implementation of string"""

class Stack:

  def __init__(self):
    self.stack = "" #initialize empty string

  #push operation
  def push(self,ch):
    self.stack += ch #add character at end 

#pop operation
  def pop(self):
    if self.is_empty():
      return "Stack is Empty"
    
    top = self.stack[-1]
    self.stack = self.stack[:-1]
    return top
   
    #peek operation
#peek
  def peek(self):
    if self.is_empty():
      return "Stack is Empty"
    return self.stack[-1]
  
  #check if empty
  def is_empty(self):
    return len(self.stack) == 0
  
  #Display stack
  def display(self):
    return self.stack
  
#testing

s = Stack()

s.push('a')
s.push('b')
s.push('c')

print("stack: ",s.display())
# print("pop: ",s.pop())
print("peek: ",s.peek())
print("Stack: ",s.display  ())
