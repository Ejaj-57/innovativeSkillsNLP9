'''
# String is a data type

1. core 
2. indexing 
3. slicing
-> string immutable



'''

text = "Python Prgramming"
print(text[0])

# slicing string[start:end:step]
print(text[0:6:2])
reverse_text = text[::-1]
print(reverse_text)

# String manupulation
msg = "Welcome to Python"

print(msg.upper())
print(msg.lower)

print(msg.upper().find("O")) 

# string.startswith() always return boolean value
print(msg.lower().startswith("welcome")) 

# cleaning string
dirty_data = "apple, banana, cherry, data"
print(dirty_data.strip())

# splitting
print(dirty_data.split(", "))

# join() -> it returns iterable to string
fruits = dirty_data.split(",")
print(" | ".join(fruits))



