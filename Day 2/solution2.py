def checkDecreasing(line):
    for i in range(len(line) - 1):
        if line[i] <= line[i + 1] or (line[i] - line[i + 1]) > 3:
            return i  
    return -1  

def checkRising(line):
    for i in range(len(line) - 1):
        if line[i] >= line[i + 1] or (line[i + 1] - line[i]) > 3:
            return i  
    return -1  

def try_remove_and_check(line, check_func):
    if check_func(line) == -1:
        return True
    
    for i in range(len(line)):
        modified_line = line[:i] + line[i + 1:]
        if check_func(modified_line) == -1:
            return True
    
    return False 

# Open the file
with open('input2.txt', 'r') as file:
    num_of_safe = 0
    for line in file:
        line = list(map(int, line.split()))
        
        if checkDecreasing(line) == -1 or checkRising(line) == -1:
            num_of_safe += 1
        else:
            if try_remove_and_check(line, checkDecreasing) or try_remove_and_check(line, checkRising):
                num_of_safe += 1

print(num_of_safe)
