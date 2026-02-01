"""DICTIONARY METHODS"""

my_dict = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3",
}
print("Original Dictionary:", my_dict)
print("Dictionary Items:", my_dict.items())
print("Dictionary Keys:", my_dict.keys())
print( my_dict.get("key1"))
print( my_dict.pop("key1"))
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}
mysuru_food = karnataka_food.pop("Mysuru")
print(mysuru_food)  # Output: Mysore Pak
del karnataka_food["Mangaluru"]
print(karnataka_food.keys())  # Output: dict_keys(['Bengaluru', 'Mysuru', 'Mangaluru'])

new_dishes = {"Hubballi": "Girmit"}
karnataka_food.update(new_dishes)