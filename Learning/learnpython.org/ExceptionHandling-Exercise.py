#ExceptionHandling-Exercise.py
#setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify
def get_last_name():
    try:
        return actor["last_name"]
    except KeyError:
        first_name,last_name = actor["name"].split()
        return last_name

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())