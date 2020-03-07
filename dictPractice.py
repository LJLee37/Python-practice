def do_something():
    n = 1

fruit = {
    "Apple" : 3000,
    "Melon" : 10000
}
print(fruit["Apple"])
print(len(fruit))
for i in fruit.values():
    do_something()
fruit["Lemon"] = 0
print (fruit)