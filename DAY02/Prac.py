'''Tuple is immutable and ordered'''
# t = (1,2,3,4,5)

#Access Tuple

# t = (10,20,30,40)

# print(t[::2])

"""Count of Occurrence"""

# t = (1,2,3,4,5,6,5,5,2,1)
# print(t.count(5))

"""Conv list to Tuple"""

# lst = [1,2,3]
# t = tuple(lst)

# print(t)

"""Unpacking"""

# t = (100,200,300)
# a,b,c = t
# print(a,b,c)

"""Store Student Records"""

# students = (
#   ("Nikhil",91),
#   ("Rahul",90),
#   ("Will",89)
# )

# # for name,marks in student:
# #   print (name,"scored",marks)

# topper = max(students , key=lambda x: x[1])
# print("Topper:",topper[0],"marks:",topper[1])

"""Remove Duplicates Using Tuple"""
t = (1, 2, 2, 3, 4, 4, 5)
unique = tuple(set(t))
print(unique)
