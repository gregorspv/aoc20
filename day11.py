# part 1

from copy import deepcopy

with open("day11.txt") as df:
    seats = list(map(list,df.read().splitlines()))
    n_rows = len(seats)
    n_columns = len(seats[0])

# without changing the system, append floor around the circumference in order to simplify occupied_seats
for row in range(n_rows):
    seats[row].insert(0, ".")
    seats[row].append(".")
seats.insert(0, list("."*(n_columns+2)))
seats.append(list("."*(n_columns+2)))

# find number of occupied adjacent seats
def occupied_seats(row, column, matrix):
    conditions = []
    conditions.append(matrix[row][column - 1] == "#")
    conditions.append(matrix[row][column + 1] == "#")
    conditions.append(matrix[row - 1][column - 1] == "#")
    conditions.append(matrix[row + 1][column - 1] == "#")
    conditions.append(matrix[row - 1][column + 1] == "#")
    conditions.append(matrix[row + 1][column + 1] == "#")
    conditions.append(matrix[row - 1][column] == "#")
    conditions.append(matrix[row + 1][column] == "#")

    return sum(conditions)

# print whole seat matrix
def print_seats(matrix):
    for row in range(len(matrix)):
        print("".join(matrix[row]))

def change(row, column, matrix):
    if matrix[row][column] == "L" and occupied_seats(row, column, matrix) == 0:
        return "#"
    elif matrix[row][column] == "#" and occupied_seats(row, column, matrix) >= 4:
        return "L"
    else:
        return matrix[row][column]

old_matrix = deepcopy(seats) # gimme value not reference!
new_matrix = deepcopy(seats)

for row in range(1, n_rows + 1):
    for column in range(1, n_columns + 1):
        new_matrix[row][column] = change(row, column, old_matrix)

while new_matrix != old_matrix: # break once there is no change
    # print_seats(old_matrix)

    old_matrix = deepcopy(new_matrix)
    for row in range(1, n_rows+1):
        for column in range(1, n_columns+1):
            new_matrix[row][column] = change(row, column, old_matrix)

def counter(query, matrix):
    returner = 0
    for row in range(1, n_rows+1):
        for column in range(1, n_columns+1):
            if matrix[row][column] == query:
                returner += 1

    return returner

n_occupied = counter("#", new_matrix)

print(f"The number of occupied seats is {n_occupied}.")

# part 2

def visible_seats(row, column, matrix):
    returner = 0
    # leftwards
    for seat in matrix[row][0:column][::-1]:
        if seat == "#":
            returner += 1
            break
        elif seat == "L":
            break
    # rightwards
    for seat in matrix[row][column + 1:-1]:
        if seat == "#":
            returner += 1
            break
        elif seat == "L":
            break
    # upwards
    for seat in [s[column] for s in matrix[0:row]][::-1]:
        if seat == "#":
            returner += 1
            break
        elif seat == "L":
            break
    # downwards
    for seat in [s[column] for s in matrix[row+1:-1]]:
        if seat == "#":
            returner += 1
            break
        elif seat == "L":
            break
    # NW
    for seat in [matrix[row - i][column - i] for i in range(1,min(row, column))]:
        if seat == "#":
            returner += 1
            break
        elif seat == "L":
            break
    # NE
    for seat in [matrix[row - i][column + i] for i in range(1, min(row, n_columns + 2 - column))]:
        if seat == "#":
            returner += 1
            break
        elif seat == "L":
            break
    # SE
    for seat in [matrix[row + i][column + i] for i in range(1, min(n_rows + 2 - row, n_columns + 2 - column))]:
        if seat == "#":
            returner += 1
            break
        elif seat == "L":
            break
    # SW
    for seat in [matrix[row + i][column - i] for i in range(1, min(n_rows + 2 - row, column))]:
        if seat == "#":
            returner += 1
            break
        elif seat == "L":
            break
    return returner

def change(row, column, matrix):
    if matrix[row][column] == "L" and visible_seats(row, column, matrix) == 0:
        return "#"
    elif matrix[row][column] == "#" and visible_seats(row, column, matrix) >= 5:
        return "L"
    else:
        return matrix[row][column]

old_matrix = deepcopy(seats) # gimme value not reference!
new_matrix = deepcopy(seats)

for row in range(1, n_rows + 1):
    for column in range(1, n_columns + 1):
        new_matrix[row][column] = change(row, column, old_matrix)

while new_matrix != old_matrix: # break once there is no change
    # print_seats(old_matrix)

    old_matrix = deepcopy(new_matrix)
    for row in range(1, n_rows+1):
        for column in range(1, n_columns+1):
            new_matrix[row][column] = change(row, column, old_matrix)

n_occupied = counter("#", new_matrix)
print(f"The number of occupied seats is {n_occupied}.")
