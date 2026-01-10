car = {
    "brand" : "toyata",
    "color" : "red",
    "price" : 500000
}

for i in car:
    print(i)

for i in car:
    print(car[i])

for i, j in car.items():
    print(i, j)

print(car.values())