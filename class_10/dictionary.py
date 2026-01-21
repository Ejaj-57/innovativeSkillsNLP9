'''
-> Key, Value pair
-> No need to follow any sequence
-> Dictionary is mutable
-> Iterating over a dictionary gives keys only
-> or:  for user, count in user_dict.items():
-> .append() only works on lists, not integers
-> # setdefault(username, 0) ensures the key exists with value 0 if missing


'''
# Creating a dictionary


d1 = {"a":1, "b": 2}
d2 = dict(a =1, b=2, c=3 )

data = [("id", 101), ("section", 2)]
d3 = dict(data)

keys = ("wifi", "nfc", "bluetooth")

d4 = dict.fromkeys(keys, "off")
print(d4)

# Inserting/ updating
user = {"name": "Rasel"}
user["age"] = 33
user.update(status="online")
user.update({"city":"Maymensing", "job" : "Power"})
user.update(age = 34)
print(user)

# Deleting
user1 = {
    "name": "Avijit",
    "age": 34,
    "city": "Dahamrai",
    "job": "Pharma"
}

del user1["age"]
user1_name = user1.pop("name", "not found")

# LIFO
user1.popitem()

user1.clear()
print(user1)
print(user1_name)

# Copying
newDict = user1.copy()

print(newDict)




