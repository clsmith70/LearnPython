#Sets.py
print(set("my name is Chris and Chris is my name".split()))

#set up event attendee lists
a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)
print()

#find the intersection between the sets (who attended both events)
print(a.intersection(b))
print(b.intersection(a))
print()

#find the symmetric difference (who attended only one of the events
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print()

#find the difference (who attended one and not the other)
print(a.difference(b))
print(b.difference(a))
print()

#get a list of all participants
print(a.union(b))
