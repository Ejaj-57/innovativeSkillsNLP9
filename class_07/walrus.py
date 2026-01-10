value = 13
reminder  = value%5

if reminder:
    print(f"not Divisible, reminder is {reminder}")

# walrus :=
value = 12
if reminder := value%5:
    print(reminder)
print(f"reminder: {reminder}")
