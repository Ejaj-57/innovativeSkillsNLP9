'''
Task 2: The "Pixel Flasher" (Modifying 2D Lists)
The Challenge: In computer graphics, a screen is a 2D grid of 0s (off) and 1s (on). Write a function called activate_row(screen, row_index) that takes the grid and a row number, then uses a single loop to change every pixel in that specific row to 1.
'''

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
        