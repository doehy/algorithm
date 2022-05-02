night = input()
row = int(night[1])
column = int(ord(night[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]

result = 0

for step in steps:
    r_row = row + step[0]
    c_column = column + step[1]
    if r_row >=1 and r_row <= 8 and c_column >=1 and c_column <= 8:
        result += 1
    
print(result)