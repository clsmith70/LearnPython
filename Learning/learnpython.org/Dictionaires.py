phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
print()

for name, number in phonebook.items():
    print("Phone number for %s is %d" % (name, number))

print()

# del phonebook["John"]
#phonebook.pop("John")
#print(phonebook)

# testing
phonebook["Jake"] = 938273443
phonebook.pop("Jill")

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")