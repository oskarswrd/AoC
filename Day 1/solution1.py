left_column = []
right_column = []
sums = []
diff = 0
total_sim = 0
val = 0

with open("input1.txt") as f:
    for line in f:
        left, right = line.split()  
        left_column.append(left)
        right_column.append(right)

def calc_similarity(x, list):
   occurance = 0
   x = int(x)
   for elem in list:
      if(int(elem) == x):
         occurance = occurance + 1
   return occurance * x

for i in left_column:
   num = calc_similarity(i, right_column) 
   total_sim += num 

print(total_sim)


   
'''


while (left_column and right_column):
  smallest_left = min (left_column)
  left_column.remove(smallest_left)
  smallest_right = min (right_column)
  right_column.remove(smallest_right)

  if (smallest_left > smallest_right):
    diff += int(smallest_left) - int(smallest_right)
  else:
    diff += int(smallest_right) - int(smallest_left)

'''









