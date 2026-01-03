

'''
Assignment: The "Data Sanitizer & Upgrader"
Scenario: You have a list of sensor readings. Some are valid numbers, but some are "Error" strings. You need to clean the list, modify the values, and calculate a result—all using a for i in range() loop.

readings = [12.5, "Error", 18.2, 15.0, "Error", 22.1, 10.8]


Task 1: The Cleaner (Search and Replace)
Write a for loop using range() to find every instance of the string "Error". Replace it with the number 0.0.
'''



readings = [12.5, "Error", 18.2, 15.0, "Error", 22.1, 10.8]

# clean_readings = [reading for reading in readings if isinstance(reading, (int, float))]
# print(clean_readings)

# for i in range(len(readings)):
#     if type(readings[i]) != int and type(readings[i]) !=float:
#         readings[i] = 0.0

# print(readings)

for i in range(len(readings)):
    if readings[i] == "Error":
        readings[i]=0.0

print(readings)



'''
Task 2: The Multiplier (In-place Modification)
After cleaning the list, use another for loop to increase every reading by 10% to account for a calibration offset.
(Hint: readings[i] = readings[i] * 1.1)
'''

for i in range(len(readings)):
    readings[i] = round(readings[i]* ((10/100)+1), 2)

print(readings)


'''
Task 3: The Filter (Selective Removal)
The sensor cannot record values below 15.0. Write a loop to find any value lower than 15.0 and add those low values to a new list called low_quality_log.
'''
# low_quality_log = []

# for i in range(len(readings) -1, -1, -1):
#     if readings[i] < 15:
#         low_quality_log.append(readings[i])
#         readings.pop(i)

# print(readings)
# print(low_quality_log)

low_quality_log = []
clean_higher_readings = []

for value in readings:
    if value <15:
        low_quality_log.append(value)
    
    else:
        clean_higher_readings.append(value)
    
readings = clean_higher_readings

print(readings)
print(low_quality_log)
