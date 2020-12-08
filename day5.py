# part 1
with open("day5.txt") as df:
    passes = df.read().splitlines()

seats = []

for bpass in passes:
    row=list(range(128))
    column=list(range(8))

    for r in bpass[0:7]:
        if r == "F":
            row=row[0:int((len(row)+1)/2)]
        elif r == "B":
            row=row[int((len(row)+1)/2):len(row)+1]

    for c in bpass[7:10]:
        if c == "L":
            column=column[0:int((len(column)+1)/2)]
        elif c == "R":
            column=column[int((len(column)+1)/2):len(column)+1]

    ID = 8*int(row[0]) + int(column[0])

    seats.append((row, column, ID))

print(f"The maximal ID is {str(max([i[2] for i in seats]))}")

# part 2
all_IDs = [i[2] for i in seats]
possible_IDs = [i+1 for i in all_IDs] + [i-1 for i in all_IDs]
my_ID = list(set(possible_IDs) - set(all_IDs))
IDs=[]
for id in range(len(my_ID)):
    if my_ID[id]+1 in all_IDs and my_ID[id]-1 in all_IDs:
        IDs.append(my_ID[id])
IDs = ", ".join([str(e) for e in IDs])
print(f"The seat ID is one of {IDs}.")
