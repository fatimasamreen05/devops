# Using curly braces
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)
# Using dict() function
person_alt = dict(name="Bob", age=25, city="Los Angeles")
print(person_alt)
# Accessing Values:
name = person["name"]  # Accessing the value for the key 'name'
age = person.get("age")  # Another way to access the value
print(name)
print(age)
# Adding or Updating Items:
person["email"] = "alice@example.com"  # Adding a new key-value pair
person["age"] = 31  # Updating the value of an existing key
print(person)
# Removing Items:
email = person.pop("email")  # Removes 'email' key and returns its value
del person["city"]  # Deletes the key 'city'
last_item = person.popitem()  # Removes and returns the last inserted item
print(person)
# Iterating Over a Dictionary:

# Looping through keys
print("Keys:")
for key in person.keys():
    print(key)

# Looping through values
print("\nValues:")
for value in person.values():
    print(value)

# Looping through key-value pairs
print("\nKey-Value Pairs:")
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

# Checking if a Key Exists:
if "name" in person:
    print("\nName is present")
