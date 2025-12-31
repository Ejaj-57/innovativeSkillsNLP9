# Assignment: Data Sanitizer & Upgrader

readings = [12.5, "Error", 18.2, 15.0, "Error", 22.1, 10.8]

# Task 1: The Cleaner (Search and Replace)
# Replace every "Error" with 0.0
for i in range(len(readings)):
    if readings[i] == "Error":
        readings[i] = 0.0

print("After Task 1 (cleaned):", readings)


# Task 2: The Multiplier (In-place Modification)
# Increase every reading by 10% and keep 2 digits after decimal
# readings[i] = readings[i] * 1.1

for i in range(len(readings)):
    readings[i] = round(readings[i] * 1.1, 2)

print("After Task 2 (+10%):", readings)


# Task 3: The Filter (Selective Removal)
# Values below 15.0 are invalid:
# - store them in low_quality_log
# - remove them from readings

low_quality_log = []

for i in range(len(readings) - 1, -1, -1):
    if readings[i] < 15.0:
        low_quality_log.append(readings[i])
        readings.pop(i)

print("Final readings (>= 15.0):", readings)
print("Low quality log (< 15.0):", low_quality_log)
