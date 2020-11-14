# List comprehension
li = [num**2 for num in range(0, 100) if num % 2 is 0]
print(li)

# Set comprehension
se = {num**2 for num in range(0, 100) if num % 2 is 0}
print(se)

# Dictionary comprehension
simp = {
    'a': 1,
    'b': 2
}
# new_dict = {k*2: v**2 for k, v in simp.items() if k*2 == 'bb'}
new_dict = {v: v**2 for v in [1, 2, 3]}
print(new_dict)

# Exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)
