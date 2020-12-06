# part 1
from functools import reduce

with open("day3.txt") as df:
    map = df.read().splitlines()

def tree_matrix(row, column):
    return map[row-1][(column % len(map[0])) - 1]

row = 1
column = 1
trees = 0

while row != len(map):
    column += 3
    row += 1

print(f"The total number of trees hit is {str(trees)}")

# part 2
def reset():
    return 1, 1, 0 #row, column, trees

def sloper(right, down):
    global row, column, trees

    while row != len(map):
        row += down
        column += right
        if tree_matrix(row, column) == "#":
            trees += 1

tree = []

row, column, trees = reset()
sloper(1,1)
tree.append(trees)

row, column, trees = reset()
sloper(3,1)
tree.append(trees)

row, column, trees = reset()
sloper(5,1)
tree.append(trees)

row, column, trees = reset()
sloper(7,1)
tree.append(trees)

row, column, trees = reset()
sloper(1,2)
tree.append(trees)

print(f"The multiple is {str(reduce(lambda a, b: a*b, tree))}")
