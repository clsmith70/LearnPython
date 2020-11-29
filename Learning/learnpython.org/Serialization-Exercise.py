#Serialization-Exercise.py
import json

# fix this function so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary
    return salaries

# test code
salaries =  '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
#decoded_salaries = json.loads(new_salaries)
print(new_salaries["Alfred"])
print(new_salaries["Jane"])
print(new_salaries["Me"])