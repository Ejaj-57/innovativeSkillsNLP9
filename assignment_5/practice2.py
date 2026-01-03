readings = [12.5, "Error", 18.2, 15.0, "Error", 22.1, 10.8]

for i in range(len(readings)):
    if readings[i] == "Error":
        readings[i] = 0.0

print(readings)

for i in range(len(readings)):
    readings[i] *= (1.1)
    readings[i] = round(readings[i], 2)

print(readings)