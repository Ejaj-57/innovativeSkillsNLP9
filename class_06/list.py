people = ["alice", "bob", "charlie"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 1, 2.0, True]

for i in range(len(people)):
    print(people[i])

for i in people:
    print(i)
name = 'ejaj'
for i in name:
    print(i)

for i in mixed:
    print(i)
    print(type(i))

print(people[1])
people.append("ejaj")
people.extend(['rasel', 'avijit'])
people.insert(1, 'warid')
people.remove('warid')
people.pop(5)

del people[3 : len(people)]
print(people)





 
