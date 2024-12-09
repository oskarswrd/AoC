import operator
from itertools import product

# Open and read the input file
with open('input7.txt', 'r') as file:
    input_string = file.read()
    lines = input_string.splitlines()


ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv
}

def evaluate_expression_with_combinations(input_string):
    correct_instances = 0

    result, operands = input_string.split(":")  
    result = int(result.strip())  
    print(f"Expected Result: {result}")
    
    clean_string = operands.strip().split()  
    operand_list = list(map(int, clean_string))  

    operator_combinations = product(ops.keys(), repeat=len(operand_list) - 1) 

    for operators in operator_combinations:
        current_result = operand_list[0]  
        expression = str(current_result)  

        
        for i, operator in enumerate(operators):
            current_result = ops[operator](current_result, operand_list[i + 1])  
            expression += f" {operator} {operand_list[i + 1]}"  

        
        rounded_result = round(current_result)  

       
        if rounded_result == result:
            correct_instances += 1  

        
        print(f"Expression: {expression}, Rounded Result: {rounded_result}")

    return correct_instances

def part1():
    total = 0
    for line in lines:
        total += evaluate_expression_with_combinations(line)  
    print(f"Total correct instances: {total}")

def main():
    part1()

main()
