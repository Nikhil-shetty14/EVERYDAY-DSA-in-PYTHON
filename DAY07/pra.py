numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Total sum:", total)

numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print("Doubled List:", doubled)

foods = ["Dosa", "Idli", "Vada", "Bisibelebath"]

for food in foods:
    print(f"I like {food}")

    names = ["Anand", "Geetha", "Kumar"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)

data = "apple,banana,mango"
fruits = data.split(",")
print(fruits)