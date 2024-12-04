import numpy as np

with open('input4.txt', 'r') as file:
    input_string = file.read()
    lines = input_string.splitlines()

cols = len(lines[0])
rows = len(lines)
occurances = 0
x_mas_count = 0

matrix = np.array([list(line) for line in lines]) 

target_word = "XMAS"
target_length = len(target_word)

def search_horizontal(r, c, word, matrix):
    global occurances
    target_word = word
    target_length = len(word)
    # Forward (Right)
    if c + target_length <= cols: 
        if all(matrix[r][c + i] == target_word[i] for i in range(target_length)):
            occurances += 1
    # Backward (Left)
    if c - target_length + 1 >= 0: 
        if all(matrix[r][c - i] == target_word[i] for i in range(target_length)):
            occurances += 1

def search_vertical(r, c, word, matrix):
    global occurances
    target_word = word
    target_length = len(word)
    # Down (Vertical)
    if r + target_length <= rows: 
        if all(matrix[r + i][c] == target_word[i] for i in range(target_length)):
            occurances += 1
    # Up (Vertical)
    if r - target_length + 1 >= 0:
        if all(matrix[r - i][c] == target_word[i] for i in range(target_length)):
            occurances += 1

def search_diagonal(r, c, word, matrix): 
    global occurances
    target_word = word
    target_length = len(word)
    # Down-Right diagonal
    if r + target_length - 1 < rows and c + target_length - 1 < cols:
        if all(matrix[r + i][c + i] == target_word[i] for i in range(target_length)):
            occurances += 1

    # Up-Right diagonal
    if r - target_length + 1 >= 0 and c + target_length - 1 < cols:
        if all(matrix[r - i][c + i] == target_word[i] for i in range(target_length)):
            occurances += 1

    # Down-Left diagonal
    if r + target_length - 1 < rows and c - target_length + 1 >= 0:
        if all(matrix[r + i][c - i] == target_word[i] for i in range(target_length)):
            occurances += 1

    # Up-Left diagonal
    if r - target_length + 1 >= 0 and c - target_length + 1 >= 0:
        if all(matrix[r - i][c - i] == target_word[i] for i in range(target_length)):
            occurances += 1


def search_x_mas(r, c, matrix):
    diagonal = 0
    global x_mas_count

    if matrix[r][c] == 'A':
        if r - 1 >= 0 and c - 1 >= 0 and r + 1 < rows and c + 1 < cols:
            if matrix[r-1][c-1] == 'M' and matrix[r+1][c+1] == 'S':
                diagonal += 1

        if r - 1 >= 0 and c + 1 < cols and r + 1 < rows and c - 1 >= 0:
            if matrix[r-1][c+1] == 'M' and matrix[r+1][c-1] == 'S':
                diagonal +=1

        if r + 1 < rows and c - 1 >= 0 and r - 1 >= 0 and c + 1 < cols:
            if matrix[r+1][c-1] == 'M' and matrix[r-1][c+1] == 'S':
                diagonal += 1

        if r + 1 < rows and c + 1 < cols and r - 1 >= 0 and c - 1 >= 0:
            if matrix[r+1][c+1] == 'M' and matrix[r-1][c-1] == 'S':
                diagonal += 1
    if(diagonal == 2):
        x_mas_count += 1 
# Part 1
def part1():
    global occurances
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'X':  # If we find 'X', search in all directions
                search_horizontal(r, c,"XMAS", matrix)
                search_vertical(r, c, "XMAS", matrix)
                search_diagonal(r, c, "XMAS", matrix)
    print("Part1 \n The word XMAS appears: " + str(occurances) + " times\n")

def part2():
    global x_shapes
    for r in range(rows):
      for c in range(cols):
          search_x_mas(r, c, matrix)
    print("Part2 \n Amount of MAS-X-shapes are: " + str(x_mas_count))

def main():
    part1()
    part2()

main()
