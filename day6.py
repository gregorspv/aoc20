# part 1
groups = []

with open("day6.txt") as df:
    file = df.read().splitlines()
    intermediary = []
    for e in range(len(file)):
        if file[e] == "":
            groups.append(intermediary)
            intermediary = []
        else:
            intermediary.append(file[e])
            if e == len(file) - 1:
                groups.append(intermediary)

count = 0
for group in groups:
    count += len(set.union(*map(set, group)))

print(f"The count is {str(count)}")

# part 2
count = 0
for group in groups:
    count += len(set.intersection(*map(set, group)))

print(f"The count is {str(count)}")