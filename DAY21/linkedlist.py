class LinkedList:

  def __init__(self):
    self.data = "" #store full as String

  #Insert at end 
  def insert(self,value):
    if not self.data:
      self.data = value
    else:
      self.data += "->" + value

    #Delete last node
  def delete_last(self):
      if not self.data:
        return "list is empty"
      
      parts = self.data.split("->")

      if len(parts) == 1:
        self.data = ""
      else:
        parts.pop()
        self.data = "->".join(parts)

    #Display
  def display(self):
      if not self.data:
        return "Empty List"
      return self.data + "->None"
    
#testing

l1 = LinkedList()
l1.insert("a")
l1.insert("b")
l1.insert("c")

print(l1.display())

l1.delete_last()
print(l1.display())

l1.insert("d")
print(l1.display())