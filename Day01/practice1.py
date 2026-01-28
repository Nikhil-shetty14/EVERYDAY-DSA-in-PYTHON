
# 
'''Number Guessing Game'''
# import random

# secret = random.randint(1,100)
# attempts = 0

# print("Guess the number")

# while True:
#   guess = int(input("Enter your Guess:"))
#   attempts += 1

#   if guess > secret:
#     print("Too High")
#   elif guess < secret:
#     print("Too Low")  
#   else:
#     print(f"Congratulations! You've guessed the number {secret} in {attempts} attempts.")
#     break



"""Palindrome Check"""

# text = input("Enter a string: ")

# if text == text[::-1]:
#   print("Palindrome")
# else:
#   print("Not a palindrome")

"""simple calculator"""

# num1 = int(input("Enter num 1 : "))
# num2 = int(input("Enter num 2 : "))

# op = int(input("1.add\n2.sub\n3.mul\n4.div\n Enter operation num: "))

# if op == 1:
#   print(num1 + num2)

# elif op == 2:
#   print(num1 - num2)

# elif op == 3:
#   print(num1 * num2)

# elif op == 4:
#   print(num1 / num2)

# else: 
#   print("Pls enter correct num")
#   # 


'''Factorial of a number'''
# n =  int(input("Enter a num: "))

# fact = 1

# for i in range(1,1+n):
#   fact *= i

# print(fact)



'''Check prime no'''

# n = int(input("Enter the a no: "))

# if n <= 1:
#   print("Not a prime No")
# else:
#   for i in range(2,n):
#     if n % i == 0:
#       print("not Prime")
#       break

#   else:
#     Print("prime")


"""fibonacci"""

# n= int(input("How many Num"))

# a,b = 0 ,1
# for _ in range(n):
#       print(a, end=" ")
#       a,b = b, a + b


'''Sum of Digits '''

# num = int(input("Enter number: "))
# total = 0

# while num > 0:
#   total += num % 10
#   num //=10

# print("Sum of Digits:", total)



"""Reverse """
# num = int(input("Enter number: "))
# rev =0

# while num > 0:
#   rev = rev * 10 + num % 10
#   num//=10
# print("Reversed Number:", rev)

'''Armstrong number'''

num = int(input("Enter number: "))
order = len(str(num))
temp = num
total = 0

while temp > 0:
  digit= temp % 10
  total += digit ** order
  temp //=10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")