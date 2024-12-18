my_dict = {"Никита": 158, "Серега": 375, "Макс": 250}
print (my_dict)
print (my_dict["Никита"])
print (my_dict.get("Гоша"))
my_dict.update({"Петя": 400, "Вася": 300})
del my_dict ["Серега"]
print (my_dict)

my_set = {3.14, "Пиндосы", 4, 9, 3.14, 9}
print(my_set)
my_set.add((7,5))
my_set.discard(4)
print(my_set)