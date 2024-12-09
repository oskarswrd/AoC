import numpy as np

with open('input6.txt', 'r') as file:
    input_string = file.read()
    lines = input_string.splitlines()

cols = len(lines[0])
rows = len(lines)

matrix = np.array([list(line) for line in lines]) 

directions = ['>', '<', '^', 'v']
current_direction = ''

print("Matrix before walking:\n " + str(matrix))



def findCursor(matrix):
    global current_direction
    for row in range(rows):
        for col in range(cols):
            current_elem = matrix[row][col]
            if current_elem in directions:
                current_direction = current_elem
                return current_direction, (row, col)

    return None  

def part1():    
    current_direction, (curr_row, curr_col) = findCursor(matrix)
    next_elem = ''
  
    if current_direction == '^': 
        while curr_row > 0:
            next_elem = matrix[curr_row - 1][curr_col]  
            if next_elem == '#': 
                break
            matrix[curr_row, curr_col] = 'X'

            curr_row -= 1
            matrix[curr_row, curr_col] = current_direction

def main():
    part1()
    print("Matrix after walking:\n " + str(matrix))

main()
