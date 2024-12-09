import numpy as np

with open('input6.txt', 'r') as file:
    input_string = file.read()
    lines = input_string.splitlines()

cols = len(lines[0])
rows = len(lines)

matrix = np.array([list(line) for line in lines])

directions = ['>', 'v', '<', '^']
current_direction = ''

print("Matrix before walking:\n" + str(matrix))

def count_X(matrix):
    x_counter = 0  
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'X':
                x_counter += 1
    return x_counter

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
    global matrix, current_direction
    current_direction, (curr_row, curr_col) = findCursor(matrix)

    direction_vectors = {
        '>': (0, 1),  # Move right
        'v': (1, 0),  # Move down
        '<': (0, -1), # Move left
        '^': (-1, 0)  # Move up
    }
    
    def turn_right(direction):
        return directions[(directions.index(direction) + 1) % 4]

    print(f"Starting position: ({curr_row}, {curr_col}) with direction {current_direction}")
    
    while True:
        row_delta, col_delta = direction_vectors[current_direction]
        next_row, next_col = curr_row + row_delta, curr_col + col_delta
        
        if 0 <= next_row < rows and 0 <= next_col < cols:
            next_elem = matrix[next_row, next_col]
        
            
            if next_elem == '#':
                current_direction = turn_right(current_direction)  
                continue  
            matrix[curr_row, curr_col] = 'X' 
            curr_row, curr_col = next_row, next_col
            matrix[curr_row, curr_col] = current_direction  
        else:
            print("Reached the edge of the map, stopping.")
            break

def main():
    part1()
    print("Matrix after walking:\n" + str(matrix))
    print("Number of spots visited " + str(count_X(matrix)))

main()
