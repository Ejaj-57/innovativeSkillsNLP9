'''
tuple is immutable

'''
# packing
grads = ("A", "B", "C")
# unpacking
(first, second, third) = grads

(first, *second) = grads
print(second)

print(grads)
print(first, second)

myTuple = ("Rasel", [1, 2, 3], "Warid", "Rasel")
myTuple[1][0] = 120
print(myTuple)
myTuple.count("Rasel")
myTuple.index("Rasel")

# membership
print("Rasel" in myTuple)