
# Task:1
all_grades = [
[88, 92, 70], # Student 0 
[45, 80, 77], # Student 1 (Has a 45!) 
[99, 100, 95] # Student 2
]

def check_failing(grades_grid):
    for index ,grades in enumerate(grades_grid):
        for grade in grades:
            if grade < 50:
                print(f"Student {index} failed a subject!")
                break

check_failing(all_grades)

# Task: 2
'''
The Challenge: In computer graphics, a screen is a 2D grid of 0s (off) and 1s (on). Write a function called activate_row(screen, row_index) that takes the grid and a row number, then uses a single loop to change every pixel in that specific row to 1.
'''

# monitor = [
# [0, 0, 0], 
#  [0, 0, 0], 
# [0, 0, 0]
# ]

# def activate_row(screen, row_index):
#     for i, 
#     for i in range(len(row_index)):
#         row_index[i] = 1
#     print(screen)

# activate_row(monitor, 0)

monitor = [
[0, 0, 0], 
 [0, 0, 0], 
[0, 0, 0]
]

def activate_row(screen, row_index):
    for i in range(len(screen[row_index])):
        screen[row_index][i] = 1

activate_row(monitor, 1)

print(monitor)
        
