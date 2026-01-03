'''
Task 1: The "Grade Scanner" (2D Lists & Functions)
The Challenge: You have a 2D list where each inner list represents a student's scores in different subjects. Write a function check_failing(grades_grid) that prints "Student [Index] failed a subject!" if any of their scores are below 50.
'''

all_grades = [
[88, 92, 70], # Student 0 
 [45, 80, 77], # Student 1 (Has a 45!) 
 [99, 100, 95] # Student 2
]

def check_failing(grades_grid):
    for index, grades in enumerate(grades_grid):
        for grade in grades:
            if grade < 50:
                print(f"Student {index} failed a subject!")
                break


check_failing(all_grades)
    