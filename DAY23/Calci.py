
def add(a,b):
  return a + b

def sub(a,b):
  return a-b
  
def mul(a,b):
  return a * b
  
def div(a,b):
  if b == 0:
    return "Error: Division by zero"
  return a / b
  
def menu():
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Quit")

  
while (True):
  
  menu()

  choice = int(input("Enter ur choice: "))

  if choice in {1,2,3,4}:
      
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))


  if choice == 1:
    print("Result: ", add(a,b))
  elif choice == 2:
    print("Result: ", sub(a,b))
  elif choice == 3:
    print("Result: ", mul(a,b))
  elif choice == 4:
    print("Result: ", div(a,b))
  elif choice == 5:
    print("Quit")
    break
  else:
    print("Invalid choice")

      