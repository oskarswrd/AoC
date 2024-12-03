import re
total_mul = 0


# Part 1 #
def mul_tuple(mulstring):
  tuple_string = mulstring[3:]
  first_num = eval(tuple_string)[0]
  second_num = eval(tuple_string)[1]
  mul = first_num * second_num

  return mul
# ------- # 

# Part 2  #
with open('input3.txt', 'r') as file:
  instruction_enabled = True 
  file_content = file.read()
  match = re.findall(r"mul\(\d+,\d+\)|don\'t\(\)|do\(\)", file_content)
  if(match): 
    print(match)
    for i in match:
        if "don't" in i:
            instruction_enabled = False
        elif "do" in i:
            instruction_enabled = True
        else:
           if instruction_enabled:
              total_mul = total_mul + mul_tuple(i)
  print("The total is: ",total_mul)

  # ------ # 