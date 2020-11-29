# Map.py
## single iterable
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)
print()

## mutiple iterables
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1,7))) #try passing range(1,3), only 2 results will be returned

print(result)
print()

## zip() function
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers)) # what if they aren't the same size?

print(results)
print()

## custom zip() function
results2 = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)