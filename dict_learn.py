fruits = {
    "mango": "a delicious fruit"
}

veg = {
    "lady finger": "my favourite"
}

print(fruits, veg)

new_dict = {**fruits, **veg}
# new_dict = fruits | veg

print(fruits, veg, new_dict)