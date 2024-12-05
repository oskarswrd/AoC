import re

correct_order = []
counter = 0
swap_counter = 0

with open('input5.txt', 'r') as file:
    input_string = file.read()
    lines = input_string.splitlines()

pattern = re.compile(r'^\d+\|\d+$')

filtered_lines = [line for line in lines if pattern.match(line)]
test_data = [line for line in lines if not pattern.match(line)]

test_data = [line for line in test_data if line.strip() != '']


for i in range(len(filtered_lines)):
    filtered_lines[i] = filtered_lines[i].split('|')


def checkRule(line, rule):
    line_elements = line.split(',')


    if rule[0] not in line_elements or rule[1] not in line_elements:
        return None  


    index_0 = line_elements.index(rule[0])
    index_1 = line_elements.index(rule[1])


    if index_0 > index_1:
        line_elements[index_0], line_elements[index_1] = line_elements[index_1], line_elements[index_0]
        modified_line = ','.join(line_elements)
        print(f"Swapped line: {modified_line}")  
        return False 
    else:
        return True


def part1():
    global counter

    valid_lines = []

    for line in test_data:
        valid = True

        for rule in filtered_lines:
            if checkRule(line, rule) is False:
                valid = False
                break  
      
        if valid:
            valid_lines.append(line)

    for line in valid_lines:
        elements = line.split(',')
        middle_point_index = len(elements) // 2
        middle_value = int(elements[middle_point_index])

        print(f"Middle value of line '{line}' is: {middle_value}")
        counter += middle_value

    print(f"Total counter value: {counter}")


def part2():
    global swap_counter

    valid_lines = []
    swapped = []

    for line in test_data:
        line_elements = line.split(',')
        valid = True

        for rule in filtered_lines:
            if checkRule(line, rule) is False:

                index_0 = line_elements.index(rule[0])
                index_1 = line_elements.index(rule[1])
                line_elements[index_0], line_elements[index_1] = line_elements[index_1], line_elements[index_0]

                valid = False
                break  


        if not valid:
            swapped.append(','.join(line_elements))
        else:
            valid_lines.append(line)


    for line in swapped:
        elements = line.split(',')
        middle_point_index = len(elements) // 2
        middle_value = int(elements[middle_point_index])

        print(f"Swapped line: {line}")
        swap_counter += middle_value
        print(f"Total swap counter: {swap_counter}")

def main():
    part1() 
    part2()

main()
